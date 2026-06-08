import random
import logging

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import request
from django.urls import reverse
# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from cards.forms import CardCheckForm, UserRegisterForm, UserLoginForm
from cards.models import Card, User, UserProfile

logger = logging.getLogger(__name__)


# i.e. this is the query for the data
class CardListView(ListView):
    logger.info("Listing all cards..")
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created", "tag")


class CardCreateView(CreateView):
    logger.info("Creating a new card..")
    model = Card
    fields = ["question", "answer", "box", "tag"]
    success_url = reverse_lazy("card-create")  # reverse_lazy allows to refer to the view by its name card-create


class CardUpdateView(CardCreateView, UpdateView):
    logger.info("Updating card..")
    success_url = reverse_lazy("card-list")  # once the card is updated, go to the list of all cards view


class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        # return Card.objects.filter(box=self.kwargs["box_num"])
        return Card.objects.filter(box=self.kwargs["box_num"]).prefetch_related("tag").annotate(
            tag_name=F("tag__tag")
        )

    def get_context_data(self, **kwargs):
        logger.info("Fetching context data for BoxView")
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]

        # NB we create/assign a new dict key that will be passed to the template and use it inside the template
        #   this is no longer used but decided to keep it there as an example. It can be used in the template as
        #   {% for card in cards_in_this_box %}
        #   same with the check_card key
        context["cards_in_this_box"] = self.get_queryset()

        if self.object_list:  # there might be no cards left in the current box
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        logger.info("Checking if the CardCheckForm is valid")
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            logger.info("CardCheckForm is valid, data: %s", form.cleaned_data)
            card.move(form.cleaned_data["solved"])
        return redirect(request.META.get("HTTP_REFERER"))


class RegisterNewUserView(CreateView):
    template_name = "user/user_register_crispy.html"
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("card-list")
    fail_url = reverse_lazy('register-new-user')

    def post(self, request, *args, **kwargs):
        logger.info("New user registration was submitted.")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("New user registration form is valid and saved. Name: %s | Email: %s | Username: %s",
                        form.cleaned_data.get('name'),
                        form.cleaned_data.get('email'),
                        form.cleaned_data.get('username'))
            user = form.instance
            name = form.cleaned_data['name']
            messages.success(request, f"Thank you for registering, {name}.")
            return HttpResponseRedirect(self.success_url)
        else:
            error_message = form.errors.as_json()
            logger.error("there's an error: %s. Name: %s | Email: %s | Username: %s",
                         error_message, form.cleaned_data.get('name'),
                         form.cleaned_data.get('email'),
                         form.cleaned_data.get('username'))
            context = {
                'form': form,
                'error_message': f"Form is not valid. Please correct the errors: {error_message}",
            }
            return self.render_to_response(context)


class UserLoginView(LoginView):
    logger.info("Trying to log in with user's information.")
    template_name = "user/user_login_crispy.html"
    model = User
    authentication_form = UserLoginForm


class UserLogoutView(View):
    logger.info("Logging out with user's information.")

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect(reverse('user-login'))
        else:
            return HttpResponseRedirect(reverse('home'))


class UserProfileView(View):
    logger.info("Fetching user profile information.")

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        user_profile = get_object_or_404(User, id=request.user.id)
        context = {
            'user_profile': user_profile,
        }
        return render(request, 'user/user_profile.html', context)

    def has_module_permission(self, request):
        return True  # You can customize this based on your permission requirements


class Home(ListView):
    template_name = "user/index.html"
