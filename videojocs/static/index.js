$( document ).ready(function() {
    var platformSelected = 0;
    $('#search_user').on('keyup', function(){
        $.ajax({
            url: '/plataformesde/'+$("#search_user").val(),
            success: function(data){
                if(typeof data != "object"){
                    $("#search_table").addClass("d-none");
                    $("#user_not_found").removeClass("d-none");
                }
                else{
                    $("#tbody-searchuser").empty()
                    $("#search_table").removeClass("d-none")
                    $("#user_not_found").addClass("d-none")
                    $.each(data, function(index, platform) {
                        if(platform!=""){
                            var row = $('<tr>');
                            $('<td>').text(platform.name).appendTo(row);
                            $('<td>').text(platform.date).appendTo(row);
                            row.appendTo($("#tbody-searchuser"))
                        }
                    });
                }

            }
        });
    });
    $('.addVideogame').click(function (){
        let id = $(this).attr("data-platform-id");
        let name = $(this).attr("data-platform-name");
        $("#addFormVideogame").attr("action", "addVideogames/"+parseInt(id))
        $("#platformOption").val(name)
    });
    $('.updatePlatform').click(function (){
        console.log("ssss")
        let id = $(this).attr("data-id")
        let name = $(this).attr("data-name")
        let date = $(this).attr("data-date")
        $("#editFormPlatform").attr("action", "edit/"+parseInt(id))
        $("#name").val(name)
        const dateParse = new Date(dateConvert(date));
        $("#date").val(dateParse.toISOString().slice(0, 10))
    });
    $("#user-to-platform").click(function (){
        console.log(platformSelected)
        $("#addUserToPlatform").attr('action', 'add/'+platformSelected+'/'+$("#userSelected").val())
    })
    $(".addUserToGame").click(function (){
        platformSelected = $(this).attr("data-id");
    })

    function dateConvert(date){

      const partesFecha = date.split(" de ");
      const dia = partesFecha[0];
      const mes = obtainMonthNumber(partesFecha[1]);
      const anio = partesFecha[2];

      return `${anio}-${mes}-${dia}`;

      function obtainMonthNumber(mes) {
        let numeroMes;

          switch (mes.toLowerCase()) {
            case "enero":
              numeroMes = 1;
              break;
            case "febrero":
              numeroMes = 2;
              break;
            case "marzo":
              numeroMes = 3;
              break;
            case "abril":
              numeroMes = 4;
              break;
            case "mayo":
              numeroMes = 5;
              break;
            case "junio":
              numeroMes = 6;
              break;
            case "julio":
              numeroMes = 7;
              break;
            case "agosto":
              numeroMes = 8;
              break;
            case "septiembre":
              numeroMes = 9;
              break;
            case "octubre":
              numeroMes = 10;
              break;
            case "noviembre":
              numeroMes = 11;
              break;
            case "diciembre":
              numeroMes = 12;
              break;
            default:
              numeroMes = null;
          }

          return numeroMes;
        }
    }

});