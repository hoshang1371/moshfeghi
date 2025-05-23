import { getCookie } from './index.js';

const csrftoken = getCookie('csrftoken');

const url ="http://127.0.0.1:8000/"

const delete_listOfPostAddress_list = url+"post_info/PostAddress_delete_list_of_buy/"

const sendSmsForVarifyUrl = url+"post_info/send_code_for_varify_mobile_address"

export async function delete_comment(id,token) {
    const response = await fetch((`${url}products/api/DeleteCustomerComment/${id}/`), {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        }
    });
    // const resData = 'resource deleted...';
    const resData = await response;

    return resData;
}

export async function add_comment(token,product_id,text,parent) {
    let data = {
        product: product_id,
        text: text,
        parent: parent
    };
    const response = await fetch((`${url}products/api/PostCustomerComment/`), {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        },
        body: JSON.stringify(data)
    });
    // const resData = 'resource deleted...';
    const resData = await response;

    return resData;
}


export async function liked_comment(token,comment_id) {
    // let data = {
    //     product: product_id,
    //     text: text,
    //     parent: parent
    // };
    const response = await fetch((`${url}products/api/GetLikesCustomerComment/${comment_id}`), {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        },
        // body: JSON.stringify(data)
    });
    // const resData = 'resource deleted...'; .json()
    const resData = await response;

    return resData;
}


export async function delete_OrderDetails(id,token) {
    const response = await fetch((`${url}order/Delete_product_orderDetail/${id}/`), {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        }
    });
    // const resData = 'resource deleted...';
    const resData = await response;

    return resData;
}

export async function delete_OrderDetails_All(token) {
    const response = await fetch((`${url}order/Order_product_delete_list_of_buy`), {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        }
    });
    // const resData = 'resource deleted...';
    const resData = await response;

    return resData;
}

export async function sendToOrderDetails(token,id,count) {
    let data = {
        id : id,
        count : count
    };
    const response = await fetch((`${url}order/update_for_buy/`), {
        method: 'PUT',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        },
        body: JSON.stringify(data)
    });
    // const resData = 'resource deleted...';
    const resData = await response;

    return resData;
}


export async function sendAllToOrderDetails(token,sendData) {
    // let data = {
    //     id : id,
    //     count : count
    // };
    const response = await fetch((`${url}order/product_orders_details_List_buy/`), {
        method: 'PUT',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        },
        body: JSON.stringify(sendData)
    });
    // const resData = 'resource deleted...';
    const resData = await response;

    return resData;
}

export async function delete_listOfPostAddress(id,token) {
    const response = await fetch((delete_listOfPostAddress_list+id), {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        }
    });
    // const resData = 'resource deleted...';
    const resData = await response;
    return resData;
  }

// ! sesnd sms
  
export async function sendSmsForVarify(token,mobNum) {
    let data = {mobNum: mobNum};
    const response = await fetch((sendSmsForVarifyUrl), {
        // method: 'GET',
        method: "POST",
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': token,
        },
        body: JSON.stringify(data)
    });
    // const resData = 'resource deleted...';

    // const resData = await response.json();
    // return resData;
    
    const resData = await response;
    return resData;
  }
