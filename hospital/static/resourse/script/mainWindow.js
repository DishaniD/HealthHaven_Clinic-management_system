
window.onload = function () {

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    });

    valid = "2px solid #28a745";
    invalid = "2px solid #dc3545";
    initial = "1px solid #6c757d";

    // console.log(session.getObject("loginuser"));
	if(session.getObject("loginuser") != null){
        loggedUserName = session.getObject("loginuser").loginusername;
        lblLogUser.innerHTML = loggedUserName;
        loggedUser = httpRequest("/user/getuser/"+loggedUserName , "GET" );
        session.setObject('activeuser', loggedUser);

        lblLoggedUserAs.innerHTML = loggedUser.employeeId.designationId.name;
        session.setObject('activeuser', loggedUser);

        if(loggedUser.employeeId != undefined){
            if(loggedUser.employeeId.photo != null) {
                profileImage.src = atob(loggedUser.employeeId.photo);
               // loadchangepassword();
            }
            else{
                profileImage.src = 'resourse/image/user.jpg';
              //  loadchangepassword();
            }
        }else {
            profileImage.src = 'resourse/image/user.jpg';
          //  loadchangepassword();
        }
    }else
		 window.location.href = "http://localhost:8080/login";



    /* ------------------------------------------------------------------------
    Side-Bar, Menu-Bar, Quick-Access is disabled According to the Privilege
    -------------------------------------------------------------------------  */

    if(session.getObject("activeuser").employeeId.id!=1) {
        //loged user select module
        modulelist = httpRequest("../module/list/listbyuser?userid=" + session.getObject("activeuser").id, "GET");
        //all module
        menuitemlist = httpRequest("../module/list","GET");

        dislist = listCompera(menuitemlist,modulelist,"id","name");

        for (x in dislist) {
            mname = dislist[x].name;
            console.log(mname);
            if ( document.getElementById(mname)!= null)
                document.getElementById(mname).remove();
            if (document.getElementsByClassName(mname).length != 0){
                document.getElementsByClassName(mname)[0].style.display = "none";
            }
            }

        }


    /* -------------------------------------------------------------  */

}

$(document).ready(function () {


    $('#dismiss, .overlay').on('click', function () {
        $('#sidebar').removeClass('active');
        $('.overlay').removeClass('active');
    });

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').addClass('active');
        $('.overlay').addClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});

function btnSignoutMC() {
    swal({
        title: "Do you want to sign out?",
        text: " ",
        icon: "warning",
        buttons: true,
        closeOnClickOutside: false
    }).then((willDelete) => {
        if (willDelete) {
            swal({
                title: "Sign Out Successful",
                text: " ",
                icon: "success",
                timer: 1500,
                buttons: false,
                closeOnClickOutside: false
            }).then(() => {
                window.location.assign('/logout');
            });

        }
    });
}


/*
function loadchangepassword() {
    changePassword = new Object();
    oldChangePassword = null;

    changePassword.username = session.getObject('activeuser').userName;

    txtUsernameView.innerHTML = changePassword.username;
    txtCurrentPassword.value = "";
    txtNewPassword.value = "";
    txtConfirmPassword.value = "";
}

function getErrors() {
    var errors = "";

    if (txtCurrentPassword.value == "") {
        errors = errors + "\n" + "Current password is not entered";
        txtCurrentPassword.style.border = invalid;
    }

    if (txtNewPassword.value == "") {
        errors = errors + "\n" + "New password is not entered";
        txtNewPassword.style.border = invalid;
    }

    if (txtConfirmPassword.value == 0) {
        errors = errors + "\n" + "Confirm password is not entered";
        txtConfirmPassword.style.border = invalid;
    }

    return errors;
}

function btnSaveChangePasswordMC() {
    var errors = getErrors();
    if (errors == "") {
        swal({
            title: "Are you sure to change password of following user?",
            text: "Username : " + changePassword.username,
            icon: "warning",
            buttons: true,
            closeOnClickOutside: false
        }).then((willDelete) => {
            if (willDelete) {
               // var response = httpRequest("/changepassword", "POST", changePassword);
                var response = "0";
                if (response == "0") {
                    swal({
                        title: "Saved Successfully",
                        text: " System Going to Logout",
                        icon: "success",
                        timer: 1500,
                        buttons: false,
                        closeOnClickOutside: false
                    }).then(() => {

                        window.location.assign('/logout');
                    });
                } else {
                    swal({
                        title: "Failed to change password",
                        text: "Response - " + response,
                        icon: "error",
                        closeOnClickOutside: false
                    });
                }
            }
        });
    } else {
        // Error Message - Invalid Data or Empty Fields
        swal({
            title: "Failed to add",
            text: "Please fill in all required fields with valid data",
            icon: "error",
            closeOnClickOutside: false
        });
    }
}
*/