$(document).ready(function() {
    $(".order-now").click(function() {
        const varietyId = $(this).data("variety-id");
        $.ajax({
            type: "GET",
            url: `/products/get_variety/${varietyId}/`,
            success: function(variety) {
                $("#orderProductName").text(variety.name);
                $("#orderProductImage").attr("src", variety.image);
                $("#orderProductDescription").text(variety.description);
                $("#variety_id").val(variety.id);
                $("#available_stock").text(variety.stock);
                $("#id_quantity").val(1);
                $("#total_price").text(variety.retail_price);
                $("#stock_message").hide();
                $("#orderPopup").show();
            },
            error: function(xhr, status, error) {
                console.error("Failed to get variety details:", xhr, status, error);
            }
        });
    });

    $("#orderForm").submit(function(event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = $(this).serialize();
        const availableStock = parseInt($("#available_stock").text(), 10);
        const quantity = parseInt($("#id_quantity").val(), 10);

        if (quantity > availableStock) {
            $("#stock_message").text("Insufficient stock available").show();
            return;
        }

        $.ajax({
            type: "POST",
            url: `/orders/place_order/`,
            data: formData,
            success: function(response) {
                if (response.status === 'success') {
                    alert("Order placed successfully!");
                    $("#orderPopup").hide();
                    location.reload(); // Reload the page to reflect updated stock
                } else {
                    $("#stock_message").text(response.message).show();
                }
            },
            error: function(xhr, status, error) {
                console.error("Failed to place order:", xhr, status, error);
                const response = xhr.responseJSON;
                if (response && response.message) {
                    $("#stock_message").text(response.message).show();
                } else {
                    alert("Failed to place order");
                }
            }
        });
    });

    $("#id_quantity").on("input", function() {
        const price = parseFloat($("#total_price").text());
        const quantity = parseInt($(this).val(), 10);
        const total = price * quantity;
        $("#total_price").text(total.toFixed(2));
    });
});

function closePopup() {
    $("#orderPopup").hide();
}
