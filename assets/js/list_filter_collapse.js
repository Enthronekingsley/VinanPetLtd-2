////;(function($){ $(document).ready(function(){
////    $('#changelist-filter').children('h3').each(function(){
////        var $title = $(this);
////        $title.click(function(){
////            $title.next().slideToggle();
////        });
////    });
////  });
////})(django.jQuery);
//
//
//<script type="text/javascript">
//    jQuery(document).ready(function($){
//        $('<div id="show-filters" style="float: right;"><a href="#">Show Filters</a></p>').prependTo('div.actions');
//        $('#show-filters').hide();
//        $('#changelist-filter h2').html('<a style="color: white;" id="hide-filters" href="#">Filter &rarr;</a>');
//
//        $('#show-filters').click(function() {
//            $('#changelist-filter').show('fast');
//            $('#changelist').addClass('filtered');
//            $('#show-filters').hide();
//        });
//
//        $('#hide-filters').click( function() {
//            $('#changelist-filter').hide('fast');
//            $('#show-filters').show();
//            $('#changelist').removeClass('filtered');
//        });
//    });
//</script>

(function($){
ListFilterCollapsePrototype = {
    bindToggle: function(){
        var that = this;
        this.$filterTitle.click(function(){
            that.$filterContent.slideToggle();
            that.$list.toggleClass('filtered');
        });
    },
    init: function(filterEl) {
        this.$filterTitle = $(filterEl).children('h2');
        this.$filterContent = $(filterEl).children('h3, ul');
        $(this.$filterTitle).css('cursor', 'pointer');
        this.$list = $('#changelist');
        this.bindToggle();
    }
}
function ListFilterCollapse(filterEl) {
    this.init(filterEl);
}
ListFilterCollapse.prototype = ListFilterCollapsePrototype;

$(document).ready(function(){
    $('#changelist-filter').each(function(){
        var collapser = new ListFilterCollapse(this);
    });
});
})(django.jQuery);
