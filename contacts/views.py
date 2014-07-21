from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.urlresolvers import reverse 
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from contacts.models import Contact 
import forms 

 

class ListContactView(ListView):

	model = Contact 
	template_name = 'contact_list.html'



class CreateContactView(CreateView):

	model = Contact
	template_name = 'edit_contact.html'
	form_class = forms.ContactForm

	def get_success_url(self):
		return reverse('contact-list')  

	def get_context_data(self, **kwargs):
	    context = super(CreateContactView, self).get_context_data(**kwargs)
	    context['action'] = reverse('contacts-new')
	    return context
	  


class UpdateContactView(UpdateView):

	model = Contact
	template_name = 'edit_contact.html'
	form_class = forms.ContactForm

	def get_success_url(self):
		return reverse('contact-list')

	def get_context_data(self, **kwargs):
	    context = super(UpdateContactView, self).get_context_data(**kwargs)
	    context['action'] = reverse('contacts-edit', 
	    							 kwargs={'pk': self.get_object().id})
	    return context
	

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class ContactView(DetailView):

    model = Contact
    template_name = 'contact.html'


class EditContactAddressView(UpdateView):

	model = Contact
	template_name = 'edit_address_html'
	form_Clas = forms.ContactAddressFormSet

	def get_success_url(self):
		return self.get_object().get_absulate_url()

		

