const addBoton = document.querySelectorAll('.carr');
    addBoton.forEach((clikButton) => {
    clikButton.addEventListener('click', Clicked);
});

const divcarro = document.querySelector('.divcarro');

function Clicked(event) {
const button = event.target;
const item = button.closest('.i');

const itemTitle = item.querySelector('.i-nom').textContent;
const itemPrice = item.querySelector('.i-pre').textContent;
const itemImage = item.querySelector('.i-im').src;
insterAlCarro(itemTitle, itemPrice, itemImage);
}


function insterAlCarro(itemTitle, itemPrice, itemImage) {
    const fila = document.createElement('div');
    const contenidoDiv = `
    <div class="row shoppingCartItem">
        <div class="col-6">
            <div class="shopping-cart-item d-flex align-items-center h-100 border-bottom pb-2 pt-3">
                <img src=${itemImage} class="shopping-cart-image">
                <h6 class="shopping-cart-item-title shoppingCartItemTitle text-truncate ml-3 mb-0">${itemTitle}</h6>
            </div>
        </div>
        <div class="col-2">
            <div class="shopping-cart-price d-flex align-items-center h-100 border-bottom pb-2 pt-3">
                <p class="item-price mb-0 shoppingCartItemPrice">${itemPrice}</p>
            </div>
        </div>
        <div class="col-4">
            <div
                class="shopping-cart-quantity d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">
                <input class="shopping-cart-quantity-input shoppingCartItemQuantity" type="number"
                    value="1">
                <button class="btn btn-danger buttonDelete" type="button">X</button>
            </div>
        </div>
    </div>`;

    fila.innerHTML = contenidoDiv;
    divcarro.append(fila)
}
function actualizarTotal(){
    let total = 0;
    const compraTotal = document.querySelector('.totalCompra');
    console.log("actualizarTotal -> compraTotal", compraTotal);

};
