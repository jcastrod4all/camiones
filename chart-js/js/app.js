$(document).ready(function() {
    $.ajax({
        url:"http://localhost/2cursophp/chart-js/data.php",
        method: "GET",
        success: function(data){
            console.log(data);
            var count = [];
            var id = [];

            for(var i in data) {
                id.push(data[i].id);
                count.push("Day of register" + data[i].reg_date);
            }

            var chartdata = {
                labels: count,
                datasets: [
                    {
                        label: 'Register Passengers',
                        backgroundColor: 'rgba(200, 200, 200, 0.75)',
                        borderColor: 'rgba(200, 200, 200, 0.75)',
                        hoverBackgroundColor: 'rgba(200, 200, 200, 1)',
                        hoverBorderColor: 'rgba(200, 200, 200, 1)',
                        data: id
                    }
                ]
            };

            var ctx = $("#mycanvas");

            var barGraph = new Chart(ctx, {
                type: 'pie',
                data: chartdata
            });
        },
        error:function(data) {
            console.log(data);
        }
    });
});