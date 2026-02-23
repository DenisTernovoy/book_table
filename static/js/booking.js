$(document).ready(function() {
    // Функция для загрузки доступных столиков
    function loadAvailableTables() {
        var date = $('#id_date').val();
        var time = $('#id_time').val();

        if (date && time) {
            $.ajax({
                url: '{% url "booking:available_tables" %}',
                data: {
                    'date': date,
                    'time': time
                },
                success: function(data) {
                    $('#id_table').empty();
                    $.each(data, function(index, table) {
                        $('#id_table').append($('<option>', {
                            value: table.id,
                            text: table.number
                        }));
                    });
                    $('#id_table').prop('disabled', false); // Разблокируем выбор столика
                }
            });
        } else {
            $('#id_table').prop('disabled', true); // Блокируем выбор столика
        }
    }

// Проверка: есть ли значения в #id_table
    if ($('#id_table').children('option').length === 0) {
        // Дополнительное условие если #id_table пуст
        $('#id_table').empty().append('<option value="">Столиков нет</option>');
        // Здесь можете добавить логику, например, показать сообщение для пользователя
    }

    // Загружаем доступные столики при изменении даты и времени
    $('#id_date, #id_time').change(loadAvailableTables);

    // Блокируем выбор столика изначально
    $('#id_table').prop('disabled', true);
});

