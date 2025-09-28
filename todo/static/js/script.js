"use strict"

window.onload = function () {
    let addbtn = document.getElementById("addbtn");
    addbtn.onclick = add_task;

    let delbtns = document.getElementsByClassName("delbtn");
    for (let btn of delbtns) {
        btn.onclick = function () {
            let todo_id = this.getAttribute("data-id");
            del_task(todo_id)
        }
    }


};

// 追加
async function add_task() {
    const title = document.getElementById("task_title").value;
    if (!title) {
        alert("入力してください")
        return
    };

    // flaskの /add にPOSTリクエストを送信
    try {
        const response = await fetch("/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ title: title })
        });

        const result = await response.text();
        console.log("サーバーからの応答", result);
        alert("タスクが入力されました");
        window.location.reload();
    }
    catch (error) {
        console.error('エラー:', error);
    };
};

// 削除
async function del_task(todo_id) {
    if (!confirm("本当に削除しますか")) {
        return
    };

    // flaskの /delete にPOSTリクエストを送信
    try {
        const response = await fetch("/delete", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ id: todo_id })
        });


        // const result = await response.text();
        if (response.ok) {
            alert("タスクを削除しました");
            // console.log("サーバーからの応答", result);
            window.location.reload();
        }
        else {
            alert("削除に失敗しました")
        };

    }
    catch (error) {
        console.error('エラー:', error);
    };
};