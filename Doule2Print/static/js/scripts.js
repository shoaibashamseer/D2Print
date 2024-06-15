function openOrderForm(varietyId, varietyName, retailPrice, wholesalePrice) {
    var customerType = '{{ customer.is_wholesale }}';
    document.getElementById('variety_id').value = varietyId;
    document.getElementById('product_name').innerText = 'Product: ' + varietyName;
    var price = (customerType === 'True') ? wholesalePrice : retailPrice;
    document.getElementById('price').innerText = 'Price: $' + price;
    document.getElementById('orderFormModal').style.display = 'block';
}

function closeOrderForm() {
    document.getElementById('orderFormModal').style.display = 'none';
}

function submitOrder(event) {
    event.preventDefault();
    var form = document.getElementById('orderForm');
    var formData = new FormData(form);

    fetch("{% url 'place_order' %}", {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        closeOrderForm();
    })
    .catch(error => console.error('Error:', error));
}
