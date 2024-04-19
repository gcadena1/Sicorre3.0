<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recursos Humanos</title>
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/sankey.js"></script>
    <script src="https://code.highcharts.com/modules/organization.js"></script>
</head>
<body>
    <div class="Organi">

    </div>
    <h1>Organigrama</h1>
    {% for nombre,usuario in resultados %}
    <h1>{{ usuario }}</h1>
    <!-- <h1>{{ nombre }}</h1> -->
    {% endfor %}
    
</body>
    <script src="//code.jquery.com/jquery-1.12.4.js"></script>
    <script src="//cdn.datatables.net/1.10.16/js/jquery.dataTables.min.js"></script>
    <script src="//cdn.datatables.net/1.10.16/js/dataTables.bootstrap4.min.js"></script>
    <script>
        $(document).ready(function(){
            Highlights.chart('Organi',{

            });
        });
    </script>
</html>