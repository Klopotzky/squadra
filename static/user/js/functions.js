jQuery(function ($) {
    $(document).ready(function() {
        // sidebar        
        $('.sidebar-toggle').on('click', function() {
            $('.logo .name, .menu > a > span, .sidebar-toggle').toggle();
            $('#sidebar').toggleClass('open');
        });

        // select2
        $.fn.select2.defaults.set("placeholder", "Wybierz...");
        $.fn.select2.defaults.set("language", "pl");
        $('.select2').select2();

        // edycja projektu
        function hideEdit(edit) {
          edit.find('form').slideUp(300, function() {
            edit.removeClass('open');
            edit.hide();
          });
        }

        $('.project .edit').on('click', function() {
          edycja = $('#edit-' + $(this).parent().parent().parent().attr('id'));
          if(!edycja.hasClass('open')) {
            $('.project-edit.open form').hide();
            $('.project-edit').removeClass('open');
            $('.project-edit').hide();
            edycja.addClass('open');
            edycja.show();
            edycja.find('form').slideDown(300);
          } else {
            hideEdit(edycja);
          }         
        });

        $('.project-edit .cancel').on('click', function(e) {
          e.preventDefault();
          hideEdit(edycja);         
        });

        $('.project-edit .project-save').on('click', function() {
          edycja = $('.project-edit.open');
          // tu trzeba bedzie zrobic funkcje, ktora zapisze zmiany wprowadzone w edycji
          hideEdit(edycja); 
        });

        // popup
        $('.popup-open').on('click', function() {
          if($(this).hasClass('add-member')) {
            $('.popup .new-project-form').hide();
            $('.popup .add-member-form').show();
          }
          if($(this).hasClass('new-project')) {
            $('.popup .new-project-form').show();
            $('.popup .add-member-form').hide();
          }
          if($(this).hasClass('issue-details')) {
            $('.popup .issue-details-pop').show();
          }
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
          elem = $(this).text();
          direct = $(this).val();
          $('#dictAndFile').load(
            "ajax_storage_content/?next_dict=" + elem + "&direct=" + direct
          );
        });

        $('#downDict').on('click', function() {
          elem = $(this).text();
          direct = $(this).val();
          $('#dictAndFile').load(
            "ajax_storage_content/?next_dict=" + elem + "&direct=" + direct
          );
        });

      ////////////////////////WORKFLOW//////////////////////////////////////////

      $('.issue-details').on('click', function() {
          id = $(this).val();
          $('#issue-details-pop').load(
                  "issue_details/?issue-id=" + id
          );
      });

    });
});
