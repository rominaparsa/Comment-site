function Setdates(id, title, caption) {
    $("#id_ask_id").val(id);
    $("#id_title").val(title);
    $("#id_caption").val(caption);
    $(".save-data").show();
}

function CreateDates() {
    $("#id_ask_id").val('0');  // صفر بذار که فرم بفهمه افزودنه
    $("#id_title").val('');
    $("#id_caption").val('');
    $(".result").addClass('d-none').hide().html("");
    $(".save-data").show();
}

function PrepareDelete(id) {
    $("#id_ask_id_delete").val(id);  // اصلاح شد اینجا
}

function escapeHtml(text) {
    return text
        .replace(/&/g, "&amp;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
}

function GetData() {
    $.ajax({
        type: "POST",
        url: "/dataajaxs/readAsk",
        data: $("#frm-getdata").serialize(),
        beforeSend: function () {
            $(".wite").removeClass("d-none").html("در حال دریافت...");
        },
        success: function (result) {
            $(".wite").html("");
            let obj;
            try {
                obj = JSON.parse(result);
            } catch (e) {
                $(".wite").html("خطا در دریافت اطلاعات.");
                return;
            }

            if (obj.length > 0) {
                let trstr = "";
                for (let i in obj) {
                    let row = obj[i]["fields"];
                    let id = obj[i]["pk"];
                    trstr += `<tr>
                        <td>${escapeHtml(row["title"])}</td>
                        <td>${escapeHtml(row["caption"])}</td>
                        <td>${row["Created"]}</td>
                        <td>
                            <button type="button" class="btn btn-primary btn-sm" onclick='Setdates("${id}", "${escapeHtml(row["title"])}", "${escapeHtml(row["caption"])}")' data-toggle="modal" data-target="#askModal">ویرایش</button>
                            <button type="button" class="btn btn-danger btn-sm" onclick='PrepareDelete("${id}")' data-toggle="modal" data-target="#askModalDelet">حذف</button>
                        </td>
                    </tr>`;
                }
                $(".body-table").html(trstr);
            } else {
                $(".body-table").html("<tr><td colspan='4' class='text-center'>اطلاعاتی برای نمایش وجود ندارد</td></tr>");
            }
        },
        error: function () {
            $(".wite").html("خطا در دریافت اطلاعات!").addClass("alert-danger");
        }
    });
}

$(document).ready(function () {
    GetData();

    $("#Search").on("keyup", function () {
        GetData();
    });

    $(".save-data").click(function (e) {
        e.preventDefault();
        $(".result").removeClass("d-none").html("در حال ارسال...").show();

        $.ajax({
            type: "POST",
            url: "/dataajaxs/saveAsk",
            data: $("#ask-form").serialize(),
            success: function (result) {
                if (result === "true") {
                    $(".result").html("ثبت اطلاعات انجام شد.").removeClass("alert-danger").addClass("alert-info");
                    $('#askModal').modal('hide');
                    GetData();
                } else if (result === "exists") {
                    $(".result").html("خطا: سوالی با این عنوان وجود دارد.").removeClass("alert-info").addClass("alert-danger");
                } else {
                    $(".result").html("خطا در ثبت اطلاعات.").removeClass("alert-info").addClass("alert-danger");
                }
            },
            error: function () {
                $(".result").html("خطای ارتباط با سرور.").removeClass("alert-info").addClass("alert-danger");
            }
        });
    });

    $(".accepted-delete").click(function (e) {
        e.preventDefault();
        $(".result-delete").removeClass("d-none").html("در حال حذف...").show();

        $.ajax({
            type: "POST",
            url: "/dataajaxs/deletAsk",
            data: $("#frm-delet").serialize(),
            success: function (result) {
                if (result === "true") {
                    $(".result-delete").html("سوال با موفقیت حذف شد.").removeClass("alert-danger").addClass("alert-info");
                    $('#askModalDelet').modal('hide');
                    GetData();
                } else {
                    $(".result-delete").html("حذف انجام نشد.").addClass("alert-danger");
                }
            },
            error: function () {
                $(".result-delete").html("خطای ارتباط با سرور در حذف.").removeClass("alert-info").addClass("alert-danger");
            }
        });
    });
});