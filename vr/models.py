from django.db import models
from multipage_form.models import MultipageModel

# Create your models here.
class Branch(models.Model):
    branch = models.CharField(max_length=300)

    def __str__(self):
        return self.branch

class Product(models.Model):
    product = models.CharField(max_length=300)

    def __str__(self):
        return self.product



class VinanPetLtd(MultipageModel):

    # STAGE 1 FIELDS
    transaction_Date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    entry_Date = models.DateTimeField(null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)

    #STAGE 2 FIELDS
    # TANK
    tank_1_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_1_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_1_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_1a_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_1a_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_1a_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_1b_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_1b_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_1b_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_2_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_2_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_2_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_2a_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_2a_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_2a_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_2b_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_2b_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_2b_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_3_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_3_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_3_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_4_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_4_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_4_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_5_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_5_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_5_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_6_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_6_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    tank_6_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    aGO_Tank_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    aGO_Tank_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    aGO_Tank_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    dPK_Tank_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    dPK_Tank_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    dPK_Tank_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)

    # STAGE 3 FIELDS
    # PUMP
    pump_1_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_1_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_1_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_2_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_2_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_2_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_2a_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_2a_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_2a_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_2b_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_2b_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_2b_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_3_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_3_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_3_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_3a_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_3a_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_3a_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_3b_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_3b_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_3b_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_4_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_4_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_4_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_4a_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_4a_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_4a_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_4b_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_4b_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_4b_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_5_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_5_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_5_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_6_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_6_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_6_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_7_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_7_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_7_Difference = models.DecimalField(max_digits=13, decimal_places=3, null=True, blank=True)
    pump_8_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_8_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_8_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_9_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_9_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_9_Difference = models.DecimalField(max_digits=13, decimal_places=3, null=True, blank=True)
    pump_10_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_10_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_10_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_11_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_11_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_11_Difference = models.DecimalField(max_digits=13, decimal_places=3, null=True, blank=True)
    pump_12_Opening = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_12_Closing = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pump_12_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    total_Pump_Difference = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)


    # STAGE 4 FIELDS
    expected_Cash = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    pos = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    # cash = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    expenses = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    balance = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    # amount_Deposited = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    teller_ID = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    teller = models.ImageField(upload_to="teller", null=True, blank=True)
    all_is_accurate = models.BooleanField(default=False)


