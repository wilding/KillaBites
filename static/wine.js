$(function() {

    // remove fields when the - button is clicked
    $('body').on('click', '.delete', function () {
        $(this).parent('div').remove();
    });

    // add WINERY fields when the + button is clicked
    $('body').on('click', '.add-winery', function () {
        $('<div class="array-input"><input type="text" name="winery" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-winery" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });

    // add VARIETY fields when the + button is clicked
    $('body').on('click', '.add-variety', function () {
        $('<div class="array-input"><input type="text" name="variety" maxlength="500"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-variety" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });

    // add NOTES fields when the + button is clicked
    $('body').on('click', '.add-note', function () {
        $('<div class="array-input"><input type="text" name="notes" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-note" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });

    // add PAIRINGS fields when the + button is clicked
    $('body').on('click', '.add-pairing', function () {
        $('<div class="array-input"><input type="text" name="pairings" maxlength="9999"><i class="fa fa-minus-circle delete" aria-hidden="true"></i><i class="fa fa-plus-circle add add-pairing" aria-hidden="true"></i></div>').insertAfter($(this).parent());
    });


    // filter by dropdown menu
    $('select').change(function () {
        var selected_region = $('.dropdown-region option:selected').text().replace(/ /g, "_");
        var selected_variety = $('.dropdown-variety option:selected').text().replace(/ /g, "_");
        var selected_winery = $('.dropdown-winery option:selected').text().replace(/ /g, "_");
        var selected_vintage = $('.dropdown-vintage option:selected').text().replace(/ /g, "_");
        // show/hide the clear button
        if (['Region', 'Variety', 'Winery', 'Vintage'].indexOf($(this).val()) == -1) {
            $(this).siblings().css('visibility', 'visible');
        }
        else {
            $(this).siblings().css('visibility', 'hidden');
        }
        // filter the wines (table)
        $('tbody tr').each(function () {
            if ($(this).hasClass('region-' + selected_region) === true && $(this).hasClass('variety-' + selected_variety) === true && $(this).hasClass('winery-' + selected_winery) === true && $(this).hasClass('vintage-' + selected_vintage) === true) {
                $(this).removeClass('hidden');
            } else {
                $(this).addClass('hidden');
            }
        });
        // filter the wines (pictures)
        $('.wine-container').each(function () {
            if ($(this).hasClass('region-' + selected_region) === true && $(this).hasClass('variety-' + selected_variety) === true && $(this).hasClass('winery-' + selected_winery) === true && $(this).hasClass('vintage-' + selected_vintage) === true) {
                $(this).removeClass('hide-wine');
            } else {
                $(this).addClass('hide-wine');
            }
        });

        // filter the dropdown options
        let regionClasses = [''];
        let varietyClasses = ['']
        let wineryClasses = ['']
        let vintageClasses = ['']
        // build lists of all visible classes
        $('.wine-container:visible').each(function() {
            $(this).attr('class')?.split(/\s+/).forEach(function(className) {
                if (className.startsWith('region-')) {
                    const cleaned = className.substring('region-'.length);
                    if (!regionClasses.includes(cleaned)) {
                        regionClasses.push(cleaned);
                    }
                }
                else if (className.startsWith('variety-')) {
                    const cleaned = className.substring('variety-'.length);
                    if (!varietyClasses.includes(cleaned)) {
                        varietyClasses.push(cleaned);
                    }
                }
                else if (className.startsWith('winery-')) {
                    const cleaned = className.substring('winery-'.length);
                    if (!wineryClasses.includes(cleaned)) {
                        wineryClasses.push(cleaned);
                    }
                }
                else if (className.startsWith('vintage-')) {
                    const cleaned = className.substring('vintage-'.length);
                    if (!vintageClasses.includes(cleaned)) {
                        vintageClasses.push(cleaned);
                    }
                }
            });
        });
        // filter out the dropdown options that aren't in the lists
        $('.region-selector').each(function () {
            if (!regionClasses.includes($(this).val().replace(/ /g, "_"))) {
                $(this).addClass('hidden');
            } else {
                $(this).removeClass('hidden');
            }
        });
        $('.variety-selector').each(function () {
            if (!varietyClasses.includes($(this).val().replace(/ /g, "_"))) {
                $(this).addClass('hidden');
            } else {
                $(this).removeClass('hidden');
            }
        });
        $('.winery-selector').each(function () {
            if (!wineryClasses.includes($(this).val().replace(/ /g, "_"))) {
                $(this).addClass('hidden');
            } else {
                $(this).removeClass('hidden');
            }
        });
        $('.vintage-selector').each(function () {
            if (!vintageClasses.includes($(this).val().replace(/ /g, "_"))) {
                $(this).addClass('hidden');
            } else {
                $(this).removeClass('hidden');
            }
        });
    });

    // deselect dropdown menu
    $('.fa-times-circle').click( function() {
        var select = $(this).siblings().attr('class').slice(9);
        select = select.charAt(0).toUpperCase() + select.slice(1);
        $(this).siblings().val(select).change();
    });

});
                
                