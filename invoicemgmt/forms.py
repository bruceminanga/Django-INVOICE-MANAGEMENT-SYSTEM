from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    invoice_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Invoice
        fields = ['name', 'phone_number', 'invoice_date', 'invoice_number',
                  'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                  'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
                  'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
                  'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
                  'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price',
                  'total', 'paid', 'invoice_type'
                  ]

    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name


class InvoiceSearchForm(forms.ModelForm):
    generate_invoice = forms.BooleanField(required=False)

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'name', 'generate_invoice']


class InvoiceUpdateForm(forms.ModelForm):
    invoice_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Invoice
        fields = ['name', 'phone_number', 'invoice_date', 'invoice_number',
                  'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                  'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
                  'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
                  'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
                  'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price',
                  'total', 'paid', 'invoice_type'
                  ]

        def clean_invoice_number(self):
            invoice_number = self.cleaned_data.get('invoice_number')
            if not invoice_number:
                raise forms.ValidationError('This field is required')
            return invoice_number

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if not name:
                raise forms.ValidationError('This field is required')
            return name
