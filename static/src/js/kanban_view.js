odoo.define('hr_employee_doyarushka.kanban_view',function(require){
"use strict";

var Model = require('web.Model');
var KanbanRenderer = require('web_kanban.KanbanView');


KanbanRenderer.include({

    render_grouped: function (fragment) {

        var arch = this.fields_view.arch;
        this.record_options.drag_drop = true;

        if (arch.attrs.check_drag_drop_record) {
            this.record_options.drag_drop = false;
        }

//      Call Super        
        this._super.apply(this, arguments);
//      .......
    },

});

});