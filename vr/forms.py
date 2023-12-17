from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import RadioSelect
from django import forms
from multipage_form.forms import MultipageForm, ChildForm
import calculation
from .models import VinanPetLtd
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm, PasswordChangeForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox



class ReportForm(MultipageForm):
    model = VinanPetLtd
    starting_form = "Stage1Form"

    class Stage1Form(ChildForm):
        display_name = "Transaction History"
        required_fields = ["entry_Date", "branch", "product"]
        next_form_class = "Stage2Form"


        class Meta:
            fields = ["entry_Date", "branch", "product"]
            widgets = {
                'entry_Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


    class Stage2Form(ChildForm):
        display_name = "Tank History"
        required_fields = "__all__"
        next_form_class = "Stage3Form"

        class Meta:
            fields = [
                "tank_1_Opening",
                "tank_1_Closing",
                "tank_1_Difference",
                "tank_1a_Opening",
                "tank_1a_Closing",
                "tank_1a_Difference",
                "tank_1b_Opening",
                "tank_1b_Closing",
                "tank_1b_Difference",
                "tank_2_Opening",
                "tank_2_Closing",
                "tank_2_Difference",
                "tank_2a_Opening",
                "tank_2a_Closing",
                "tank_2a_Difference",
                "tank_2b_Opening",
                "tank_2b_Closing",
                "tank_2b_Difference",
                "tank_3_Opening",
                "tank_3_Closing",
                "tank_3_Difference",
                "tank_4_Opening",
                "tank_4_Closing",
                "tank_4_Difference",
                "tank_5_Opening",
                "tank_5_Closing",
                "tank_5_Difference",
                "tank_6_Opening",
                "tank_6_Closing",
                "tank_6_Difference",
                "aGO_Tank_Opening",
                "aGO_Tank_Closing",
                "aGO_Tank_Difference",
                "dPK_Tank_Opening",
                "dPK_Tank_Closing",
                "dPK_Tank_Difference",
            ]
            widgets = {
                'tank_1_Difference': calculation.FormulaInput('tank_1_Opening-tank_1_Closing'),
                'tank_1a_Difference': calculation.FormulaInput('tank_1a_Opening-tank_1a_Closing'),
                'tank_1b_Difference': calculation.FormulaInput('tank_1b_Opening-tank_1b_Closing'),
                'tank_2_Difference': calculation.FormulaInput('tank_2_Opening-tank_2_Closing'),
                'tank_2a_Difference': calculation.FormulaInput('tank_2a_Opening-tank_2a_Closing'),
                'tank_2b_Difference': calculation.FormulaInput('tank_2b_Opening-tank_2b_Closing'),
                'tank_3_Difference': calculation.FormulaInput('tank_3_Opening-tank_3_Closing'),
                'tank_4_Difference': calculation.FormulaInput('tank_4_Opening-tank_4_Closing'),
                'tank_5_Difference': calculation.FormulaInput('tank_5_Opening-tank_5_Closing'),
                'tank_6_Difference': calculation.FormulaInput('tank_6_Opening-tank_6_Closing'),
                'aGO_Tank_Difference': calculation.FormulaInput('aGO_Tank_Opening-aGO_Tank_Closing'),
                'dPK_Tank_Difference': calculation.FormulaInput('dPK_Tank_Opening-dPK_Tank_Closing'),
            }

        def __init__(self, *args, **kwargs):
            super(ReportForm.Stage2Form, self).__init__(*args, **kwargs)
            self.fields["tank_1_Difference"].widget.attrs['readonly'] = True
            self.fields["tank_1a_Difference"].widget.attrs['readonly'] = True
            self.fields["tank_1b_Difference"].widget.attrs['readonly'] = True
            self.fields["tank_2_Difference"].widget.attrs['readonly'] = True
            self.fields["tank_2a_Difference"].widget.attrs['readonly'] = True
            self.fields["tank_2b_Difference"].widget.attrs['readonly'] = True
            self.fields["tank_3_Difference"].widget.attrs['readonly'] = True
            self.fields["tank_4_Difference"].widget.attrs['readonly'] = True
            self.fields["tank_5_Difference"].widget.attrs['readonly'] = True
            self.fields["tank_6_Difference"].widget.attrs['readonly'] = True
            self.fields["aGO_Tank_Difference"].widget.attrs['readonly'] = True
            self.fields["dPK_Tank_Difference"].widget.attrs['readonly'] = True


    class Stage3Form(ChildForm):
        display_name = "Pump History"
        required_fields = "__all__"
        next_form_class = "Stage4Form"

        class Meta:
            fields = [
                # "price",
                "pump_1_Opening",
                "pump_1_Closing",
                "pump_1_Difference",
                "pump_2_Opening",
                "pump_2_Closing",
                "pump_2_Difference",
                "pump_2a_Opening",
                "pump_2a_Closing",
                "pump_2a_Difference",
                "pump_2b_Opening",
                "pump_2b_Closing",
                "pump_2b_Difference",
                "pump_3_Opening",
                "pump_3_Closing",
                "pump_3_Difference",
                "pump_3a_Opening",
                "pump_3a_Closing",
                "pump_3a_Difference",
                "pump_3b_Opening",
                "pump_3b_Closing",
                "pump_3b_Difference",    
                "pump_4_Opening",
                "pump_4_Closing",
                "pump_4_Difference",
                "pump_4a_Opening",
                "pump_4a_Closing",
                "pump_4a_Difference",
                "pump_4b_Opening",
                "pump_4b_Closing",
                "pump_4b_Difference",
                "pump_5_Opening",
                "pump_5_Closing",
                "pump_5_Difference",
                "pump_6_Opening",
                "pump_6_Closing",
                "pump_6_Difference",
                "pump_7_Opening",
                "pump_7_Closing",
                "pump_7_Difference",
                "pump_8_Opening",
                "pump_8_Closing",
                "pump_8_Difference",
                "pump_9_Opening",
                "pump_9_Closing",
                "pump_9_Difference",
                "pump_10_Opening",
                "pump_10_Closing",
                "pump_10_Difference",  
                "pump_11_Opening",
                "pump_11_Closing",
                "pump_11_Difference",    
                "pump_12_Opening",  
                "pump_12_Closing",   
                "pump_12_Difference",  
                "total_Pump_Difference",
                # "amount",
                "price",
                "expected_Cash",
                "pos",
                # "cash",
                "expenses",
                "balance",
                # "amount_Deposited",
                "teller_ID",
                "teller",
                "all_is_accurate",
            ]
            widgets = {
                'pump_1_Difference': calculation.FormulaInput('pump_1_Closing-pump_1_Opening'),
                'pump_2_Difference': calculation.FormulaInput('pump_2_Closing-pump_2_Opening'),
                'pump_2a_Difference': calculation.FormulaInput('pump_2a_Closing-pump_2a_Opening'),
                'pump_2b_Difference': calculation.FormulaInput('pump_2b_Closing-pump_2b_Opening'),
                'pump_3_Difference': calculation.FormulaInput('pump_3_Closing-pump_3_Opening'),
                'pump_3a_Difference': calculation.FormulaInput('pump_3a_Closing-pump_3a_Opening'),
                'pump_3b_Difference': calculation.FormulaInput('pump_3b_Closing-pump_3b_Opening'),
                'pump_4_Difference': calculation.FormulaInput('pump_4_Closing-pump_4_Opening'),
                'pump_4a_Difference': calculation.FormulaInput('pump_4a_Closing-pump_4a_Opening'),
                'pump_4b_Difference': calculation.FormulaInput('pump_4b_Closing-pump_4b_Opening'),
                'pump_5_Difference': calculation.FormulaInput('pump_5_Closing-pump_5_Opening'),
                'pump_6_Difference': calculation.FormulaInput('pump_6_Closing-pump_6_Opening'),
                'pump_7_Difference': calculation.FormulaInput('pump_7_Closing-pump_7_Opening'),
                'pump_8_Difference': calculation.FormulaInput('pump_8_Closing-pump_8_Opening'),
                'pump_9_Difference': calculation.FormulaInput('pump_9_Closing-pump_9_Opening'),
                'pump_10_Difference': calculation.FormulaInput('pump_10_Closing-pump_10_Opening'),
                'pump_11_Difference': calculation.FormulaInput('pump_11_Closing-pump_11_Opening'),
                'pump_12_Difference': calculation.FormulaInput('pump_12_Closing-pump_12_Opening'),
                'total_Pump_Difference': calculation.FormulaInput('pump_1_Difference+pump_2_Difference+pump_2a_Difference+pump_2b_Difference+pump_3_Difference+pump_3a_Difference+pump_3b_Difference+pump_4_Difference+pump_4a_Difference+pump_4b_Difference+pump_5_Difference+pump_6_Difference+pump_7_Difference+pump_8_Difference+pump_9_Difference+pump_10_Difference+pump_11_Difference+pump_12_Difference'),
                'expected_Cash': calculation.FormulaInput('total_Pump_Difference*price'),
                'balance': calculation.FormulaInput('expected_Cash-(expenses+pos)'),
            }


        def __init__(self, *args, **kwargs):
            super(ReportForm.Stage3Form, self).__init__(*args, **kwargs)
            self.fields["pump_1_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_2_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_2a_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_2b_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_3_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_3a_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_3b_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_4_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_4a_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_4b_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_5_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_6_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_7_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_8_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_9_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_10_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_11_Difference"].widget.attrs['readonly'] = True
            self.fields["pump_12_Difference"].widget.attrs['readonly'] = True
            self.fields["total_Pump_Difference"].widget.attrs['readonly'] = True
            self.fields["expected_Cash"].widget.attrs['readonly'] = True
            self.fields["balance"].widget.attrs['readonly'] = True


    # class Stage4Form(ChildForm):
    #     display_name = "Cash History"
    #     required_fields = "__all__"
    #     next_form_class = "Stage5Form"

        # field_name = 'total_Pump_Difference'
        # obj = VinanPetLtd.objects.first()
        # field_object = VinanPetLtd._meta.get_field(field_name)
        # field_value = field_object.value_from_object(obj)

        # def amount_sold(self):
        #     field_name = 'total_Pump_Difference'
        #     obj = VinanPetLtd.objects.first()
        #     field_object = VinanPetLtd._meta.get_field(field_name)
        #     field_value = field_object.value_from_object(obj)
        #     return 2

        # class Meta:
        #     fields = [
        #         "price",
        #         "amount",
        #         "pos",
        #         "cash",
        #         "expenses",
        #         "balance",
        #         "amount_Deposited",
        #         "teller_ID",
        #         "teller",
        #         "all_is_accurate",
        #     ]
        #     widgets = {
        #         'balance': calculation.FormulaInput('cash-expenses'),
                # 'amount': calculation.FormulaInput('total_Pump_Difference*price'),
                # 'amount': calculation.FormulaInput("VinanPetLtd._meta.get_field('total_Pump_Difference').value_from_object(VinanPetLtd.objects.first())*price"),
                # 'amount': calculation.FormulaInput('amount()*price'),
            # }

        # def __init__(self, *args, **kwargs):
        #     super(ReportForm.Stage4Form, self).__init__(*args, **kwargs)
        #     self.fields["balance"].widget.attrs['readonly'] = True

    class Stage4Form(ChildForm):
        required_fields = "__all__"
        template_name = "report_summary.html"

        class Meta:
            fields = ["all_is_accurate"]
            labels = {"all_is_accurate": "Ready to submit to VinanPetLtd?"}



class SetPasswordForm(SetPasswordForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2', 'captcha']


class PasswordResetForm(PasswordResetForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


