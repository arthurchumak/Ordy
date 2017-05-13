!function(t){var e=function(t,e){this.init(t,e)};e.prototype={constructor:e,init:function(e,a){var i=this.$element=t(e);this.options=t.extend({},t.fn.checkbox.defaults,a),i.before(this.options.template),this.setState()},setState:function(){var t=this.$element,e=t.closest(".checkbox");t.prop("disabled")&&e.addClass("disabled"),t.prop("checked")&&e.addClass("checked")},toggle:function(){var e="checked",a=this.$element,i=a.closest(".checkbox"),n=a.prop(e),o=t.Event("toggle");0==a.prop("disabled")&&(i.toggleClass(e)&&n?a.removeAttr(e):a.prop(e,e),a.trigger(o).trigger("change"))},setCheck:function(e){var a="checked",i=this.$element,n=i.closest(".checkbox"),o="check"==e?!0:!1,s=t.Event(e);n[o?"addClass":"removeClass"](a)&&o?i.prop(a,a):i.removeAttr(a),i.trigger(s).trigger("change")}};var a=t.fn.checkbox;t.fn.checkbox=function(a){return this.each(function(){var i=t(this),n=i.data("checkbox"),o=t.extend({},t.fn.checkbox.defaults,i.data(),"object"==typeof a&&a);n||i.data("checkbox",n=new e(this,o)),"toggle"==a&&n.toggle(),"check"==a||"uncheck"==a?n.setCheck(a):a&&n.setState()})},t.fn.checkbox.defaults={template:'<span class="icons"><span class="first-icon fa fa-square-o"></span><span class="second-icon fa fa-check-square-o"></span></span>'},t.fn.checkbox.noConflict=function(){return t.fn.checkbox=a,this},t(document).on("click.checkbox.data-api","[data-toggle^=checkbox], .checkbox",function(e){var a=t(e.target);"A"!=e.target.tagName&&(e&&e.preventDefault()&&e.stopPropagation(),a.hasClass("checkbox")||(a=a.closest(".checkbox")),a.find(":checkbox").checkbox("toggle"))}),t(function(){t('[data-toggle="checkbox"]').each(function(){var e=t(this);e.checkbox()})})}(window.jQuery),!function(t){var e=function(t,e){this.init(t,e)};e.prototype={constructor:e,init:function(e,a){var i=this.$element=t(e);this.options=t.extend({},t.fn.radio.defaults,a),i.before(this.options.template),this.setState()},setState:function(){var t=this.$element,e=t.closest(".radio");t.prop("disabled")&&e.addClass("disabled"),t.prop("checked")&&e.addClass("checked")},toggle:function(){var e="disabled",a="checked",i=this.$element,n=i.prop(a),o=i.closest(".radio"),s=i.closest(i.closest("form").length?"form":"body"),c=s.find(':radio[name="'+i.attr("name")+'"]'),r=t.Event("toggle");0==i.prop(e)&&(c.not(i).each(function(){var i=t(this),n=t(this).closest(".radio");0==i.prop(e)&&n.removeClass(a)&&i.removeAttr(a).trigger("change")}),0==n&&o.addClass(a)&&i.prop(a,!0),i.trigger(r),n!==i.prop(a)&&i.trigger("change"))},setCheck:function(e){var a="checked",i=this.$element,n=i.closest(".radio"),o="check"==e?!0:!1,s=i.prop(a),c=i.closest(i.closest("form").length?"form":"body"),r=c.find(':radio[name="'+i.attr("name")+'"]'),d=t.Event(e);r.not(i).each(function(){var e=t(this),i=t(this).closest(".radio");i.removeClass(a)&&e.removeAttr(a)}),n[o?"addClass":"removeClass"](a)&&o?i.prop(a,a):i.removeAttr(a),i.trigger(d),s!==i.prop(a)&&i.trigger("change")}};var a=t.fn.radio;t.fn.radio=function(a){return this.each(function(){var i=t(this),n=i.data("radio"),o=t.extend({},t.fn.radio.defaults,i.data(),"object"==typeof a&&a);n||i.data("radio",n=new e(this,o)),"toggle"==a&&n.toggle(),"check"==a||"uncheck"==a?n.setCheck(a):a&&n.setState()})},t.fn.radio.defaults={template:'<span class="icons"><span class="first-icon fa fa-circle-o"></span><span class="second-icon fa fa-dot-circle-o"></span></span>'},t.fn.radio.noConflict=function(){return t.fn.radio=a,this},t(document).on("click.radio.data-api","[data-toggle^=radio], .radio",function(e){var a=t(e.target);e&&e.preventDefault()&&e.stopPropagation(),a.hasClass("radio")||(a=a.closest(".radio")),a.find(":radio").radio("toggle")}),t(function(){t('[data-toggle="radio"]').each(function(){var e=t(this);e.radio()})})}(window.jQuery),!function(t){"use strict";t.fn.bootstrapSwitch=function(e){var a={init:function(){return this.each(function(){var e,a,i,n,o,s,c=t(this),r="",d=c.attr("class"),h="ON",l="OFF",f=!1;t.each(["switch-mini","switch-small","switch-large"],function(t,e){d.indexOf(e)<0||(r=e)}),c.addClass("has-switch"),void 0!==c.data("on")&&(o="switch-"+c.data("on")),void 0!==c.data("on-label")&&(h=c.data("on-label")),void 0!==c.data("off-label")&&(l=c.data("off-label")),void 0!==c.data("icon")&&(f=c.data("icon")),a=t("<span>").addClass("switch-left").addClass(r).addClass(o).html(h),o="",void 0!==c.data("off")&&(o="switch-"+c.data("off")),i=t("<span>").addClass("switch-right").addClass(r).addClass(o).html(l),n=t("<label>").html("&nbsp;").addClass(r).attr("for",c.find("input").attr("id")),f&&n.html('<i class="'+f+'"></i>'),e=c.find(":checkbox").wrap(t("<div>")).parent().data("animated",!1),c.data("animated")!==!1&&e.addClass("switch-animate").data("animated",!0),e.append(a).append(n).append(i),c.find(">div").addClass(c.find("input").is(":checked")?"switch-on":"switch-off"),c.find("input").is(":disabled")&&t(this).addClass("deactivate");var p=function(t){t.siblings("label").trigger("mousedown").trigger("mouseup").trigger("click")};c.on("keydown",function(e){32===e.keyCode&&(e.stopImmediatePropagation(),e.preventDefault(),p(t(e.target).find("span:first")))}),a.on("click",function(){p(t(this))}),i.on("click",function(){p(t(this))}),c.find("input").on("change",function(e){var a=t(this),i=a.parent(),n=a.is(":checked"),o=i.is(".switch-off");e.preventDefault(),i.css("left",""),o===n&&(n?i.removeClass("switch-off").addClass("switch-on"):i.removeClass("switch-on").addClass("switch-off"),i.data("animated")!==!1&&i.addClass("switch-animate"),i.parent().trigger("switch-change",{el:a,value:n}))}),c.find("label").on("mousedown touchstart",function(e){var a=t(this);s=!1,e.preventDefault(),e.stopImmediatePropagation(),a.closest("div").removeClass("switch-animate"),a.closest(".has-switch").is(".deactivate")?a.unbind("click"):(a.on("mousemove touchmove",function(e){var a=t(this).closest(".switch"),i=(e.pageX||e.originalEvent.targetTouches[0].pageX)-a.offset().left,n=i/a.width()*100,o=25,c=75;s=!0,o>n?n=o:n>c&&(n=c),a.find(">div").css("left",n-c+"%")}),a.on("click touchend",function(e){var a=t(this),i=t(e.target),n=i.siblings("input");e.stopImmediatePropagation(),e.preventDefault(),a.unbind("mouseleave"),s?n.prop("checked",!(parseInt(a.parent().css("left"))<-25)):n.prop("checked",!n.is(":checked")),s=!1,n.trigger("change")}),a.on("mouseleave",function(e){var a=t(this),i=a.siblings("input");e.preventDefault(),e.stopImmediatePropagation(),a.unbind("mouseleave"),a.trigger("mouseup"),i.prop("checked",!(parseInt(a.parent().css("left"))<-25)).trigger("change")}),a.on("mouseup",function(e){e.stopImmediatePropagation(),e.preventDefault(),t(this).unbind("mousemove")}))})})},toggleActivation:function(){t(this).toggleClass("deactivate")},isActive:function(){return!t(this).hasClass("deactivate")},setActive:function(e){e?t(this).removeClass("deactivate"):t(this).addClass("deactivate")},toggleState:function(e){var a=t(this).find("input:checkbox");a.prop("checked",!a.is(":checked")).trigger("change",e)},setState:function(e,a){t(this).find("input:checkbox").prop("checked",e).trigger("change",a)},status:function(){return t(this).find("input:checkbox").is(":checked")},destroy:function(){var e,a=t(this).find("div");return a.find(":not(input:checkbox)").remove(),e=a.children(),e.unwrap().unwrap(),e.unbind("change"),e}};return a[e]?a[e].apply(this,Array.prototype.slice.call(arguments,1)):"object"!=typeof e&&e?void t.error("Method "+e+" does not exist!"):a.init.apply(this,arguments)}}(jQuery);