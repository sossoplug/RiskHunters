import random

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils.text import slugify

# ================ MAIN CATEGORY =========================
class MainCategory(models.Model):
    """
    Model representing a main category.
    """
    name                    = models.CharField(max_length=100, verbose_name=_("Name"))
    description             = models.TextField(verbose_name=_("Description"))
    category_img            = models.ImageField(upload_to='images/', null=True)

    updated                 = models.DateTimeField(auto_now=True)
    created                 = models.DateTimeField(auto_now_add=True)  # Changed to auto_now_add to capture the creation time only once

    class Meta:
        verbose_name        = _("Main Category")
        verbose_name_plural = _("Main Categories")
        ordering            = ['-created', '-updated']  # '- dash' indicates descending order

    def __str__(self):
        return self.name


# ================= SUB CATEGORY =========================
class SubCategory(models.Model):
    """
    Model representing a sub category.
    """
    main_category           = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='subcategories', verbose_name=_("Main Category"))  # Foreign Key to link to the Main Category
    name                    = models.CharField(max_length=100, verbose_name=_("Name"))
    description             = models.TextField(verbose_name=_("Description"))
    updated                 = models.DateTimeField(auto_now=True)
    created                 = models.DateTimeField(auto_now_add=True)  # Changed to auto_now_add to capture the creation time only once

    class Meta:
        verbose_name        = _("Sub Category")
        verbose_name_plural = _("Sub Categories")
        ordering            = ['-created', '-updated']  # '- dash' indicates descending order

    def __str__(self):
        return self.name
# ========================================================

# ================ STRATEGY ============================
class Strategy(models.Model):
    """
    Model representing a gambling strategy.
    """
    name                    = models.CharField(max_length=200, verbose_name=_("Name"))
    description             = models.TextField(verbose_name=_("Description"))
    ranking_terminated      = models.BooleanField(default=False, verbose_name=_("Ranking Terminated"))
    ranking                 = models.IntegerField(verbose_name=_("Ranking"))
    user                    = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_("User"))
    subcategories           = models.ManyToManyField(SubCategory, related_name='strategies', verbose_name=_("SubCategories"))  # Many-to-Many relationship with SubCategory
    updated                 = models.DateTimeField(auto_now=True)
    created                 = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = _("Strategy")
        verbose_name_plural = _("Strategies")
        ordering            = ['-created', '-updated']  # orderby updated then created (- dash ) means ascendent or not namean


    def __str__(self):
        return self.name
# =====================================================


# ================ REVIEW ============================
class Review(models.Model):
    """
    Model representing a review of a strategy.
    """

    user                    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    strategy                = models.ForeignKey(Strategy, on_delete=models.CASCADE, verbose_name=_("Strategy"))
    rating                  = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name=_("Rating"))
    review_text             = models.TextField(verbose_name=_("Review Text"))
    updated                 = models.DateTimeField(auto_now=True)
    created                 = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name        = _("Review")
        verbose_name_plural = _("Reviews")
        ordering            = ['-created', '-updated']  # orderby updated then created (- dash ) means ascendent or not namean

    def __str__(self):
        return f"Review by {self.user} - {self.rating}/5"
# =====================================================

# ================ INVESTMENT PLAN ============================
STRATEGY_TYPE_CHOICES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('annually', 'Annually'),
]

class InvestmentPlan(models.Model):
    """
    Model representing an investment plan.
    """
    user                      = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name                      = models.CharField(max_length=200, verbose_name=_("Name"), null=True)
    category                  = models.ForeignKey('MainCategory', on_delete=models.SET_NULL, null=True, verbose_name=_("Category"), related_name='investment_plans')
    initial_capital           = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)], verbose_name=_("Initial Capital"))
    risk                      = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name=_("Risk"))
    reward                    = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name=_("Reward"))
    risk_percent_per_position = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name=_("Risk Percent Per Position"))
    amount_risked_per_position = models.DecimalField(max_digits=5, decimal_places=2, null=True, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name=_("Risk Percent Per Position"))
    numbers_of_position       = models.IntegerField(validators=[MinValueValidator(1)], verbose_name=_("Numbers Of Position"))
    win_rate_ratio            = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name=_("Win Rate Ratio"))
    strategy_type             = models.CharField(max_length=10, choices=STRATEGY_TYPE_CHOICES, verbose_name=_("Strategy Type"))
    expected_growth_percent   = models.DecimalField(max_digits=5, decimal_places=2,  null=True, default=0, verbose_name=_("Expected Growth Percent"))
    growth_in_cash            = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0, verbose_name=_("Growth in Cash"))
    potential_cash_loss       = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0, verbose_name=_("Potential Loss in Cash"))
    potential_net_profit      = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0, verbose_name=_("Potential Net Profit"))
    profit_factor             = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0, verbose_name=_("Profit Factor"))
    public                    = models.BooleanField(default=False, verbose_name=_("Public"))
    updated                   = models.DateTimeField(auto_now=True)
    created                   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name          = _("Investment Plan")
        verbose_name_plural   = _("Investment Plans")
        ordering              = ['-created', '-updated']  # orderby updated then created (- dash ) means ascendent or not namean


    def __str__(self):
        return self.name


    def calculate_potential_loss(self):
        """
        Calculate the potential loss based on risk percent per position and number of positions.

        Returns:
            Decimal: The potential loss in cash.
        """
        potential_loss          = self.initial_capital * (self.risk_percent_per_position / 100) * self.numbers_of_position
        return potential_loss


    def calculate_linear_expected_growth(self):
        """
        Calculate the expected growth of the investment plan.

        Returns:
            Tuple: The expected growth of the investment plan in percent and cash.
        """
        win_rate_ratio_decimal              = self.win_rate_ratio / 100
        risk_percent_per_position_decimal   = self.risk_percent_per_position / 100
        loss_rate                           = 1 - win_rate_ratio_decimal

        amount_at_risk_per_trade            = self.initial_capital * risk_percent_per_position_decimal
        amount_won_per_trade                = amount_at_risk_per_trade * self.reward
        amount_lost_per_trade               = amount_at_risk_per_trade * self.risk

        net_gain_per_trade                  = (amount_won_per_trade * win_rate_ratio_decimal) - (amount_lost_per_trade * loss_rate)

        total_net_gain                      = net_gain_per_trade * self.numbers_of_position

        growth_in_cash                      = total_net_gain
        growth_in_percent                   = (growth_in_cash / self.initial_capital) * 100

        return growth_in_percent, growth_in_cash, amount_at_risk_per_trade

    def calculate_expected_compound_growth(self):
        """
        Calculate the expected compound growth of the investment plan.

        Returns:
            Tuple: The expected growth of the investment plan in percent and cash.
        """
        win_rate_ratio_decimal              = self.win_rate_ratio / 100
        risk_percent_per_position_decimal   = self.risk_percent_per_position / 100
        loss_rate                           = 1 - win_rate_ratio_decimal

        amount_at_risk_per_trade            = self.initial_capital * risk_percent_per_position_decimal
        amount_won_per_trade                = amount_at_risk_per_trade * self.reward
        amount_lost_per_trade               = amount_at_risk_per_trade * self.risk

        # Iterate over each position to compute compound growth
        current_capital                     = self.initial_capital


        for _ in range(self.numbers_of_position):
            if random.random() <= win_rate_ratio_decimal:  # A win
                current_capital             += amount_won_per_trade
            else:  # A loss
                current_capital             -= amount_lost_per_trade

        growth_in_cash                      = current_capital - self.initial_capital
        growth_in_percent                   = (growth_in_cash / self.initial_capital) * 100

        return growth_in_percent, growth_in_cash

    def calculate_net_profit(self):
        """
        Calculate the net profit by considering both the potential rewards and the potential losses.

        Returns:
            Decimal: The net profit in cash.
        """
        net_profit                                          = self.growth_in_cash - self.potential_cash_loss
        return net_profit


    def calculate_profit_factor(self):
        """
        Calculate the profit factor which is the ratio of gross profit to gross loss.

        Returns:
            Decimal: The profit factor.
        """
        gross_profit                                        = self.growth_in_cash
        gross_loss                                          = self.potential_cash_loss
        if gross_loss != 0:
            profit_factor                                   = gross_profit / gross_loss
        else:
            profit_factor                                   = 0  # or potentially some other handling for division by zero
        return profit_factor


    def save(self, *args, **kwargs):
        self.potential_cash_loss                            = self.calculate_potential_loss()
        self.expected_growth_percent, self.growth_in_cash   = self.calculate_expected_growth()
        self.potential_net_profit                           = self.calculate_net_profit()
        self.profit_factor                                  = self.calculate_profit_factor()
        super().save(*args, **kwargs)
# =========================================================


# ================ INVESTMENT PLAN  REVIEW ============================

class InvestmentPlanReview(models.Model):
    investment_plan             = models.ForeignKey(InvestmentPlan, on_delete=models.CASCADE, related_name='reviews', verbose_name=_("Investment Plan"))
    user                        = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    review_text                 = models.TextField(verbose_name=_("Review Text"))
    rating                      = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name=_("Rating"))
    created                     = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated                     = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name            = _("Investment Plan Review")
        verbose_name_plural     = _("Investment Plan Reviews")
        ordering                = ['-created', '-updated']

    def __str__(self):
        return f"Review by {self.user} - {self.rating}/5"
# =========================================================



# ============================ PROS MODEL ============================
class Pros(models.Model):
    """
    Model representing an individual pro associated with a growth model.

    Attributes:
        name (CharField):       The name of the pro.
        description (TextField): The detailed description of the pro.
    """
    name                        = models.CharField(max_length=255, verbose_name=_("Name"))
    description                 = models.TextField(verbose_name=_("Description"))
    created                     = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created At"))
    updated                     = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name            = _("Pro")
        verbose_name_plural     = _("Pros")
        ordering                = ['name']

    def __str__(self):
        return self.name


# ============================ CONS MODEL ============================
class Cons(models.Model):
    """
    Model representing an individual con associated with a growth model.

    Attributes:
        name (CharField):       The name of the con.
        description (TextField): The detailed description of the con.
    """
    name                        = models.CharField(max_length=255, verbose_name=_("Name"))
    description                 = models.TextField(verbose_name=_("Description"))
    created                     = models.DateTimeField(auto_now_add=True,  null=True, verbose_name=_("Created At"))
    updated                     = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name            = _("Con")
        verbose_name_plural     = _("Cons")
        ordering                = ['name']

    def __str__(self):
        return self.name


# ============================ GROWTH MODEL ============================
class GrowthModel(models.Model):
    """
    Model representing a growth model with associated pros and cons.

    Attributes:
        name (CharField):  The name of the growth model.
        description (TextField): The detailed description of the growth model.
        pros (ManyToManyField): The associated pros of the growth model.
        cons (ManyToManyField): The associated cons of the growth model.
    """
    name                        = models.CharField(max_length=255, verbose_name=_("Name"))
    nickname                    = models.CharField(max_length=255, null=True, verbose_name=_("Nickname"))
    slug                        = models.SlugField(max_length=255, unique=True, null=True, blank=True, verbose_name=_("Slug"))
    description                 = models.TextField(verbose_name=_("Description"))
    pros                        = models.ManyToManyField(Pros, related_name='growth_models', verbose_name=_("Pros"))
    cons                        = models.ManyToManyField(Cons, related_name='growth_models', verbose_name=_("Cons"))
    example                     = models.TextField(verbose_name=_("Example"), null=True, help_text=_("You can use HTML tags for formatting"))
    calculable                  = models.BooleanField(default=False, null=True, verbose_name=_("Calculable"))
    created                     = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created At"))
    updated                     = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name            = _("Growth Model")
        verbose_name_plural     = _("Growth Models")
        ordering                = ['name']

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


