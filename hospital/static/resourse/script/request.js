window.addEventListener("load", initialize);

//Initializing Functions

function initialize() {

    console.log("136522")
    $('.js-example-basic-single').select2({
    });

    btnAdd.addEventListener("click", btnAddMC);
    //btnClear.addEventListener("click", btnClearMC);
    //btnUpdate.addEventListener("click", btnUpdateMC);

    //cmbCustomerRegion.addEventListener("change", cmbCustomerRegionCH);

    //dteDOBirth.onchange = dteDOBirthCH;
    //txtSearchName.addEventListener("keyup", btnSearchMC);

    //privilages = httpRequest("../privilage?module=Customerrequest", "GET");

    //data services for combo boxes
    //crstatuses = httpRequest("../crstatus/list", "GET");
    cregions = httpRequest("../cregion/list", "GET");
    tourpackages = httpRequest("../tourpackage/list","GET");

    valid = "2px solid #20B2AA";
    invalid = "2px solid #FF69B4";
    initial = "2px solid #d6d6c2";
    updated = "2px solid #FFA07A";
    active = "#F0E68C";

    loadForm();
    //loadView();

}

/*function loadView() {

    //Search Area
    txtSearchName.value = "";
    txtSearchName.style.background = "";

    //Table Area
    activerowno = "";
    activepage = 1;
    var query = "&searchtext=";
    loadTable(1, cmbPageSize.value, query);
}*/

/*function loadTable(page, size, query) {
    page = page - 1;
    customerrequests = new Array();
    var data = httpRequest("/customerrequest/findAll?page=" + page + "&size=" + size + query, "GET");
    if (data.content != undefined) customerrequests = data.content;
    createPagination('pagination', data.totalPages, data.number + 1, paginate);
    fillTable('tblCustomerRequest', customerrequests, fillForm, btnDeleteMC, viewitem);
    clearSelection(tblCustomerRequest);
    selectDeleteRow();

    if (activerowno != "") selectRow(tblCustomerRequest, activerowno, active);

}*/
/*
function selectDeleteRow() {
    for (index in customerrequests) {
        if (customerrequests[index].crstatusId.name == "Deleted") {
            tblCustomerRequest.children[1].children[index].style.color = "#f00";
            tblCustomerRequest.children[1].children[index].style.border = "2px solid red";
            tblCustomerRequest.children[1].children[index].lastChild.children[1].disabled = true;
            tblCustomerRequest.children[1].children[index].lastChild.children[1].style.cursor = "not-allowed";
        }
    }
}*/

/*function paginate(page) {
    var paginate;
    if (oldcustomerrequest == null) {
        paginate = true;
    } else {
        if (getErrors() == '' && getUpdates() == '') {
            paginate = true;
        } else {
            paginate = window.confirm("Form has Some Errors or Update Values. " +
                "Are you sure to discard that changes ?");
        }
    }
    if (paginate) {
        activepage = page;
        activerowno = ""
        loadSearchedTable();
        loadForm();
    }

}*/

/*function viewitem(cus, rowno) {

    customer = JSON.parse(JSON.stringify(cus));

    tdCregno.setAttribute('value', customer.regno);
    tdCname.innerHTML = customer.cname;
    tdCnic.innerHTML = customer.nic;
    tdCmobile.innerHTML = customer.cmobile;
    tdCemail.innerHTML = customer.email;
    tdCaddress.innerHTML = customer.address;
    tdCdescription.innerHTML = customer.description;
    tdCpname.innerHTML = customer.cpname;
    tdCpmobile.innerHTML = customer.cpmobile;
    tdregdate.innerHTML = customer.regdate;
    tdCtype.innerHTML = customer.ctypeId.name;
    tdCregion.innerHTML = customer.cregionId.name;
    tdCstatus.innerHTML = customer.cstatusId.name;
    tdemployee.innerHTML = customer.employeeId.callingname;
}

function btnFormRowMC() {

    var format = cusPrintView.outerHTML;

    var newwindow = window.open();
    newwindow.document.write("<html>" +
        "<head><style type='text/css'>.google-visualization-table-th {text-align: left;}</style></head>" +
        "<body><div style='margin-top: 150px'><h1>Customer Details :</h1></div>" +
        "<div>" + format + "</div>" +
        "<script>cusPrintView.removeAttribute('style')</script>" +
        "</body></html>");
    setTimeout(function () {
        newwindow.print();
        newwindow.close();
    }, 100);
}*/

function cmbCustomerRegionCH() {
    var countrycode = JSON.parse(cmbCustomerRegion.value).code;
    txtCountryCode.value = countrycode;

    if(oldcustomerrequest != null && oldcustomerrequest.cregionId.code != countrycode){
        txtCountryCode.style.border = updated;
    }else{
        txtCountryCode.style.border = valid;
    }

}

function loadForm() {
    customerrequest = new Object();
    oldcustomerrequest = null;

    fillCombo3(cmbTourPack,"Select a Tour Package", tourpackages, "code", "name","");
    fillCombo(cmbCustomerRegion, "Select a Region", cregions, "name", "");

   /* fillCombo(cmbCRequeststatus, "", crstatuses, "name", "Pending");
    customerrequest.crstatusId = JSON.parse(cmbCRequeststatus.value);


    var today = new Date();
    var month = today.getMonth() + 1;
    if (month < 10) month = "0" + month;
    var date = today.getDate();
    if (date < 10) date = "0" + date;

    dteDOAdded.value = today.getFullYear() + "-" + month + "-" + date;
    customerrequest.addeddate = dteDOAdded.value;*/


    txtCustomerName.value = "";
    txtCountryCode.value = "";
    txtNoChilPass.value = "";
    txtNoAdultPass.value = "";
    txtMobile.value = "";
    txtEmail.value = "";
    txtComment.value = "";
    dteDORequired.value = "";

    setStyle(initial);
    $('.select2-container').css('border', initial);
    /*cmbCRequeststatus.style.border = valid;
    dteDOAdded.style.border = valid;*/

    //disableButtons(false, true, true);
}

function setStyle(style) {
    txtCustomerName.style.border = style;
    //cmbCustomerRegion.style.border = style;
    $('.select2-container').css('border', style);
    cmbTourPack.style.border = style;
    txtCountryCode.style.border = style;
    txtMobile.style.border = style;
    txtEmail.style.border = style;
    txtNoChilPass.style.border = style;
    txtNoAdultPass.style.border = style;
    txtComment.style.border = style;
    dteDORequired.style.border = style;
   /* cmbCRequeststatus.style.border = style;
    dteDOAdded.style.border = style;*/
}

/*function disableButtons(add, upd, del) {

    if (add || !privilages.add) {
        btnAdd.setAttribute("disabled", "disabled");
        $('#btnAdd').css('cursor', 'not-allowed');
    } else {
        btnAdd.removeAttribute("disabled");
        $('#btnAdd').css('cursor', 'pointer')
    }

    if (upd || !privilages.update) {
        btnUpdate.setAttribute("disabled", "disabled");
        $('#btnUpdate').css('cursor', 'not-allowed');
    } else {
        btnUpdate.removeAttribute("disabled");
        $('#btnUpdate').css('cursor', 'pointer');
    }

    if (!privilages.update) {
        $(".buttonup").prop('disabled', true);
        $(".buttonup").css('cursor', 'not-allowed');
    } else {
        $(".buttonup").removeAttr("disabled");
        $(".buttonup").css('cursor', 'pointer');
    }

    if (!privilages.delete) {
        $(".buttondel").prop('disabled', true);
        $(".buttondel").css('cursor', 'not-allowed');
    } else {
        $(".buttondel").removeAttr("disabled");
        $(".buttondel").css('cursor', 'pointer');
    }

}*/


function getErrors() {

    var errors = "";
    addvalue = "";

    if (customerrequest.fname == null)
        errors = errors + "\n" + "Customer Name is not enter";
    else addvalue = 1;

    if (customerrequest.tourpackageId == null)
        errors = errors + "\n" + "Tour Package is not selected";

    if (customerrequest.cregionId == null)
        errors = errors + "\n" + "Region is not selected";

    if (customerrequest.mobile == null)
        errors = errors + "\n" + "Mobile Number is not enter";
    else addvalue = 1;

    if (customerrequest.noofadults == null)
        errors = errors + "\n" + "Passengers are not enter";
    else addvalue = 1;

    if (customerrequest.email == null)
        errors = errors + "\n" + "Email is not enter";
    else addvalue = 1;


    return errors;

}

function btnAddMC() {
    if (getErrors() == "") {
        if (txtComment.value == "" || txtNoChilPass.value == "") {
            swal({
                title: "Are you sure to continue...?",
                text: "Form has some empty fields.....",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            }).then((willDelete) => {
                if (willDelete) {
                    savedata();
                }
            });

        } else {
            savedata();
        }
    } else {
        swal({
            title: "You have following errors",
            text: "\n" + getErrors(),
            icon: "error",
            button: true,
        });

    }
}

function savedata() {
    var comments = "None";
    if (customerrequest.comment != null){
        comments = customerrequest.comment;
    }


    var childpassengers = "0";
    if (customerrequest.noofchildren != null){
        childpassengers = customerrequest.noofchildren;
    }

    swal({
        title: "Are you sure to add following customerrequest...?",
        text:"\nCalling Name : " + customerrequest.fname +
            "\nTour Package : " + customerrequest.tourpackageId.name +
            "\nRegion : " + customerrequest.cregionId.name +
            "\nNo of Adult Passengers : " + customerrequest.noofadults +
            "\nNo of Children : " + childpassengers +
            "\nMobile : " + customerrequest.cregionId.code + customerrequest.mobile +
            "\nE-mail : " + customerrequest.email +
            "\nComments : " + comments +
            "\nRequired Date : " + customerrequest.requireddate ,
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            var response = httpRequest("/customerrequest", "POST", customerrequest);
            if (response == "0") {
                swal({
                    position: 'center',
                    icon: 'success',
                    title: 'Your work has been Done \n Save SuccessFully..!',
                    text: '\n',
                    button: false,
                    timer: 1200
                });
                loadForm();
                activerowno = 1;
                loadSearchedTable();
            } else swal({
                title: 'Save not Success... , You have following errors', icon: "error",
                text: '\n ' + response,
                button: true
            });
        }
    });

}

/*function btnClearMC() {
    //Get Cofirmation from the User window.confirm();
    checkerr = getErrors();

    if (oldcustomerrequest == null && addvalue == "") {
        loadForm();
    } else {
        swal({
            title: "Form has some values, updates values... Are you sure to discard the form ?",
            text: "\n",
            icon: "warning", buttons: true, dangerMode: true,
        }).then((willDelete) => {
            if (willDelete) {
                loadForm();
            }

        });
    }
}*/

/*function fillForm(cusreq,rowno) {
    activerowno = rowno;

    if (oldcustomerrequest == null) {
        filldata(cusreq);
    } else {
        swal({
            title: "Form has some values, updates values... Are you sure to discard the form ?",
            text: "\n",
            icon: "warning", buttons: true, dangerMode: true,
        }).then((willDelete) => {
            if (willDelete) {
                filldata(cusreq);
            }

        });
    }

}*/


/*
function filldata(cusreq) {
    clearSelection(tblCustomerRequest);
    selectDeleteRow();
    selectRow(tblCustomerRequest, activerowno, active);

    customerrequest = JSON.parse(JSON.stringify(cusreq));
    oldcustomerrequest = JSON.parse(JSON.stringify(cusreq));

    txtCustomerName.value = customerrequest.fname;
    txtCountryCode.value = customerrequest.cregionId.code;
    txtNoAdultPass.value = customerrequest.noofadults;
    txtNoChilPass.value = customerrequest.noofchildren;
    txtMobile.value = customerrequest.mobile;
    txtEmail.value = customerrequest.email;
    txtComment.value = customerrequest.comment;
    dteDORequired.value = customerrequest.requireddate;
    dteDOAdded.value = customerrequest.addeddate;


    fillCombo3(cmbTourPack, "Select Tour Package", tourpackages, "code", "name",customerrequest.tourpackageId.code);
    fillCombo(cmbCustomerRegion, "Select Region", cregions, "name", customerrequest.cregionId.name);
    cmbCustomerRegionCH();
    fillCombo(cmbCRequeststatus, "", crstatuses, "name",customerrequest.crstatusId.name );
    customerrequest.crstatusId = JSON.parse(cmbCRequeststatus.value);

    cmbCRequeststatus.disabled = false;

    disableButtons(true, false, false);
    setStyle(valid);

    if (txtComment.value == "") {
        txtComment.style.border = initial;
    }

    if (dteDORequired.value == "") {
        dteDORequired.style.border = initial;
    }
    if (txtNoChilPass.value == "") {
        txtNoChilPass.style.border = initial;
    }


}

function getUpdates() {

    var updates = "";

    if (customerrequest != null && oldcustomerrequest != null) {

        if (customerrequest.fname != oldcustomerrequest.fname)
            updates = updates + "\nCustomer Name is Changed";

        if (customerrequest.mobile != oldcustomerrequest.mobile)
            updates = updates + "\nCustomer Mobile is Changed";

        if (customerrequest.noofadults != oldcustomerrequest.noofadults)
            updates = updates + "\nNo of Passengers are Changed";

        if (customerrequest.noofchildren != oldcustomerrequest.noofchildren)
            updates = updates + "\nNo of Children Passengers are Changed";

        if (customerrequest.email != oldcustomerrequest.email)
            updates = updates + "\nEmail is Changed";

        if (customerrequest.comment != oldcustomerrequest.comment)
            updates = updates + "\nComments are Changed";

        if (customerrequest.requireddate != oldcustomerrequest.requireddate)
            updates = updates + "\nRequired Date is Changed";

        if (customerrequest.cregionId.name != oldcustomerrequest.cregionId.name)
            updates = updates + "\nRegion is Changed";

        if (customerrequest.tourpackageId.code != oldcustomerrequest.tourpackageId.code)
            updates = updates + "\nTour Package is Changed";

        if (customerrequest.crstatusId.name != oldcustomerrequest.crstatusId.name)
            updates = updates + "\nStatus is Changed";

    }

    return updates;

}

function btnUpdateMC() {
    var errors = getErrors();
    if (errors == "") {
        var updates = getUpdates();
        if (updates == "")
            swal({
                title: 'Nothing Updated..!', icon: "warning",
                text: '\n',
                button: false,
                timer: 1200
            });
        else {
            swal({
                title: "Are you sure to update following customer request details...?",
                text: "\n" + getUpdates(),
                icon: "warning", buttons: true, dangerMode: true,
            })
                .then((willDelete) => {
                    if (willDelete) {
                        var response = httpRequest("/customerrequest", "PUT", customerrequest);
                        if (response == "0") {
                            swal({
                                position: 'center',
                                icon: 'success',
                                title: 'Your work has been Done \n Update SuccessFully..!',
                                text: '\n',
                                button: false,
                                timer: 1200
                            });
                            loadForm();
                            loadSearchedTable();

                        } else swal({
                            title: 'Update not Success... , You have following errors', icon: "error",
                            text: '\n ' + response,
                            button: true
                        });
                    }
                });
        }
    } else
        swal({
            title: 'You have following errors in your form', icon: "error",
            text: '\n ' + getErrors(),
            button: true
        });

}

function btnDeleteMC(cusreq) {
    customerrequest = JSON.parse(JSON.stringify(cusreq));

    swal({
        title: "Are you sure to delete following customer request...?",
        text: "\n Customer Name : " + customerrequest.fname +
            "\n Region : " + customerrequest.tourpackageId.code ,
        icon: "warning", buttons: true, dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            var responce = httpRequest("/customerrequest", "DELETE", customerrequest);
            if (responce == 0) {
                swal({
                    title: "Deleted Successfully....!",
                    text: "\n\n  Status change to delete",
                    icon: "success", button: false, timer: 1200,
                });
                loadForm();
                loadSearchedTable();
            } else {
                swal({
                    title: "You have following erros....!",
                    text: "\n\n" + responce,
                    icon: "error", button: true,
                });
            }
        }
    });

}

function loadSearchedTable() {

    var searchtext = txtSearchName.value;

    var query = "&searchtext=";

    if (searchtext != "")
        query = "&searchtext=" + searchtext;
    //window.alert(query);
    loadTable(activepage, cmbPageSize.value, query);

}

function btnSearchMC() {
    activepage = 1;
    loadSearchedTable();
}

function btnSearchClearMC() {
    loadView();
}

function btnPrintTableMC(customerrequest) {

    var newwindow = window.open();
    formattab = tblCustomerRequest.outerHTML;

    newwindow.document.write("" +
        "<html>" +
        "<head><style type='text/css'>.google-visualization-table-th {text-align: left;} .modifybutton{display: none} .isort{display: none}</style>" +
        "<link rel='stylesheet' href='../plugin/bootstrap/css/bootstrap.min.css'/></head>" +
        "<body><div style='margin-top: 150px; '> <h1>Customer Request Details : </h1></div>" +
        "<div>" + formattab + "</div>" +
        "</body>" +
        "</html>");
    setTimeout(function () {
        newwindow.print();
        newwindow.close();
    }, 100);
}

function sortTable(cind) {
    cindex = cind;

    var cprop = tblCustomerRequest.firstChild.firstChild.children[cindex].getAttribute('property');

    if (cprop.indexOf('.') == -1) {
        customerrequests.sort(
            function (a, b) {
                if (a[cprop] < b[cprop]) {
                    return -1;
                } else if (a[cprop] > b[cprop]) {
                    return 1;
                } else {
                    return 0;
                }
            }
        );
    } else {
        customerrequests.sort(
            function (a, b) {
                if (a[cprop.substring(0, cprop.indexOf('.'))][cprop.substr(cprop.indexOf('.') + 1)] < b[cprop.substring(0, cprop.indexOf('.'))][cprop.substr(cprop.indexOf('.') + 1)]) {
                    return -1;
                } else if (a[cprop.substring(0, cprop.indexOf('.'))][cprop.substr(cprop.indexOf('.') + 1)] > b[cprop.substring(0, cprop.indexOf('.'))][cprop.substr(cprop.indexOf('.') + 1)]) {
                    return 1;
                } else {
                    return 0;
                }
            }
        );
    }
    fillTable('tblCustomerRequest', customerrequests, fillForm, btnDeleteMC, viewitem);
    clearSelection(tblCustomerRequest);
    selectDeleteRow();

    if (activerowno != "") selectRow(tblCustomerRequest, activerowno, active);


}*/
