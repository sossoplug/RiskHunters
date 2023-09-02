from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# ================ CATEGORY ============================
class Category(models.Model):
    """
    Model representing a category.
    """
    name        = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
# =========================================================

# ================ STRATEGY ============================
class Strategy(models.Model):
    """
    Model representing a gambling strategy.
    """
    name                = models.CharField(max_length=200, verbose_name=_("Name"))
    description         = models.TextField(verbose_name=_("Description"))
    ranking_terminated  = models.BooleanField(default=False, verbose_name=_("Ranking Terminated"))
    ranking             = models.IntegerField(verbose_name=_("Ranking"))
    user                = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_("User"))

    class Meta:
        verbose_name        = _("Strategy")
        verbose_name_plural = _("Strategies")

    def __str__(self):
        return self.name
# =====================================================


# ================ REVIEW ============================
class Review(models.Model):
    """
    Model representing a review of a strategy.
    """
    RATING_CHOICES = [
        ('good', _('Good')),
        ('neutral', _('Neutral')),
        ('bad', _('Bad')),
    ]

    user         = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    strategy     = models.ForeignKey(Strategy, on_delete=models.CASCADE, verbose_name=_("Strategy"))
    rating       = models.CharField(max_length=10, choices=RATING_CHOICES, default='neutral', verbose_name=_("Rating"))
    review_text  = models.TextField(verbose_name=_("Review Text"))

    class Meta:
        verbose_name        = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return f'{self.user} - {self.strategy}'
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
    user                      = models.ForeignKey(User, on_delete=models.CASCADE)
    name                      = models.CharField(max_length=200, verbose_name=_("Name"))
    category                  = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name=_("Category"))
    initial_capital           = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)], verbose_name=_("Initial Capital"))
    risk                      = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name=_("Risk"))
    reward                    = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name=_("Reward"))
    risk_percent_per_position = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name=_("Risk Percent Per Position"))
    numbers_of_position       = models.IntegerField(validators=[MinValueValidator(1)], verbose_name=_("Numbers Of Position"))
    win_rate_ratio            = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name=_("Win Rate Ratio"))
    strategy_type             = models.CharField(max_length=10, choices=STRATEGY_TYPE_CHOICES, verbose_name=_("Strategy Type"))
    expected_growth_percent   = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Expected Growth Percent"))
    growth_in_cash            = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Growth in Cash"))

    class Meta:
        verbose_name          = _("Investment Plan")
        verbose_name_plural   = _("Investment Plans")

    def __str__(self):
        return self.name

    def calculate_expected_growth(self):
        """
        Calculate the expected growth of the investment plan.

        Returns:
            Tuple: The expected growth of the investment plan in percent and cash.
        """
        win_rate_ratio_decimal  = self.win_rate_ratio / 100
        risk_reward_ratio       = self.reward / self.risk
        expected_growth         = self.initial_capital * (1 + (win_rate_ratio_decimal * risk_reward_ratio - (1 - win_rate_ratio_decimal)) / self.numbers_of_position) ** self.numbers_of_position
        growth_in_percent       = (expected_growth - self.initial_capital) / self.initial_capital * 100
        growth_in_cash          = expected_growth - self.initial_capital
        return growth_in_percent, growth_in_cash

    def save(self, *args, **kwargs):
        self.expected_growth_percent, self.growth_in_cash = self.calculate_expected_growth()
        super().save(*args, **kwargs)
# =========================================================



