document.getElementById('theme-toggle-button').onclick = function() {
    document.body.classList.toggle('light-mode');
};



$(document).ready(function(){
    var createInvestmentPlanUrl = $('#calculateForm').data('create-investment-plan-url');
    var saveInvestmentPlanUrl   = $('#calculateForm').data('save-investment-plan-url');

    $("#calculateButton").click(function(e){
        e.preventDefault();
        $.ajax({
            url: createInvestmentPlanUrl,
            type: 'POST',
            data: $('#calculateForm').serialize(),
            success: function(response){
                if(response.success){
                    $("#resultsSection").css("display", "block");
                    $("#amount_risked_per_position").text(response.amount_risked_per_position);
                    $("#expectedGrowthPercent").text(response.expected_growth_percent);
                    $("#growthInCash").text(response.growth_in_cash);
                    $("#potentialCashLoss").text(response.potential_cash_loss);
                    $("#potentialNetProfit").text(response.potential_net_profit);
                    $("#profitFactor").text(response.profit_factor);
                    $("#strategyType").text(response.strategy_type);
                } else {
                    alert(response.message);
                }
            }
        });
    });


    $("#saveButton").click(function(e){
        e.preventDefault();
        $("#saveFormSection").css("display", "block");
    });

    $("#saveFormButton").click(function(e){
        e.preventDefault();
        $.ajax({
            url: saveInvestmentPlanUrl,
            type: 'POST',
            data: $('#saveForm').serialize(),
            success: function(response){
                if(response.success){
                    alert(response.message);
                } else {
                    alert(response.message);
                }
            }
        });
    });
});

/*
*    ---  (UN/DIS)PLAY SEARCH BOX  ---
*/
$("#search_trigger").on("click", function() {
    var displayValue = $("#searchbox").css("display");

    if (displayValue === "none") {
        $("#searchbox").css("display", "block");
    } else if (displayValue === "block") {
        $("#searchbox").css("display", "none");
    }
});
/*  ---     SEARCH BOX END     ---   */