jQuery(function ($) {
    $(document).ready(function() {
        // sidebar        
        $('.sidebar-toggle').on('click', function() {
            $('.logo .name, .menu > a > span, .sidebar-toggle').toggle();
            $('#sidebar').toggleClass('open');
        });

        // popup
        $('.popup-open').on('click', function() {
            $('.popup-container').addClass('open');
        });

        $('.popup-close').on('click', function() {
            $('.popup-container').removeClass('open');
        });

        $('.popup-container').on('click', function(e) {
            var container = $('.popup-container .popup');
            if (!container.is(e.target) && container.has(e.target).length === 0) {
                $('.popup-container').removeClass('open');
            }
        });

        $('.getFile').on('click', function() {
          $(this).text(function(e, elem){
            console.log("elem " + elem);
            $.ajax({
              url: '/squadra_app/ajax_open_file',
              data: {
                'open_file_name': elem
              },
              dataType: 'json',
              success: function (data) {
                console.log(data.content)
                $('.popup-container').removeClass('open');
                for (var instance in CKEDITOR.instances)
                    CKEDITOR.instances[instance].updateElement();
        
                var temp = CKEDITOR.instances[instance].setData(data.content);
              }
            });
          });
        });

        $('#saveFile').on('click', function() {
            for (var instance in CKEDITOR.instances)
              CKEDITOR.instances[instance].updateElement();

            var temp = CKEDITOR.instances[instance].getData();

            $.ajax({
              url: '/squadra_app/ajax_html_text',
              data: {
                'text': temp
              },
              dataType: 'json',
              success: function (data) {
              if (data.is_taken) {
                alert("Udalo sie zapisac plik");
              }
            }
          });
        });

        // Eksport plików
        $('#exportFiles').on('click', function() {
          console.log("jestem w funkcji");
          let values = [];
            const checkboxes = document.querySelectorAll('input[name="checkf"]:checked');
            checkboxes.forEach((checkbox) => {
              values.push(checkbox.value);
          });  
      
          console.log(values[0]);
          $.ajax({
            url: '/squadra_app/export_file/',
            traditional:true,
            data: {
              'export_fname': values
            },
            dataType: 'json',
            success: function (data) {
              console.log("sukces ");
              console.log("sukces " + data);
              if (data.is_taken) {
                alert("Udało się eksportować plik");
              }
            }
          });
        });

        //Poruszanie się po folderach. Z jakiegoś powodu blokuje się po jednym kliknięciu.
        //Tak jakby dało się użyć funkcję tylko raz
        $('.getDict').on('click', function() {
          $(this).text(function(e, elem) {
            $(this).val(function(a, direct) {
              $('#dictAndFile').load(
                "ajax_storage_content/?next_dict=" + elem + "&direct=" + direct
              );
            });
          });
        });

        $('#downDict').on('click', function() {
          $("#downDict").text(function(e, elem) {
            $("#downDict").val(function(a, direct) {
              $('#dictAndFile').load(
                "ajax_storage_content/?next_dict=" + elem + "&direct=" + direct
              );
            });
          });
        });
      });
});