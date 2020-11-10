const addBoton = document.querySelectorAll('.carr');
addBoton.forEach((clikButton) => {
    clikButton.addEventListener('click', Clicked);
});

const divcarro = document.querySelector('.shoppingCartItemsContainer');

const botonComprar = document.querySelector('.comprarButton');
botonComprar.addEventListener('click', clickcomprar());

function Clicked(event) {

    const button = event.target;
    const item = button.closest('.i');

    const itemTitle = item.querySelector('.i-nom').textContent;
    const itemPrice = item.querySelector('.i-pre').textContent;
    const itemImage = item.querySelector('.i-im').src;
    insterAlCarro(itemTitle, itemPrice, itemImage);
}

function insterAlCarro(itemTitle, itemPrice, itemImage) {
    const elem = divcarro.getElementsByClassName('.shoppingCartItemTitle');
    for (let i = 0; i < elem.length; i++) {
        if (elem[i].innerText === itemTitle) {
            let Quantity = elem[i].parentElement.parentElement.parentElement.querySelector(
                '.cantidadTitulos');
            Quantity.value++;
            actualizarTotal();
            return;
        }
    }


    const fila = document.createElement('div');
    const contenidoDiv = `
    <div class="row itemsDelCarrito pipi">

    <div class="col-6">
            <div class="form-row shopping-cart-item d-flex align-items-center h-100 border-bottom pb-2 pt-3">
                
            <img src=${itemImage} class="shopping-cart-image">
                
            <h6 class="form-group shopping-cart-item-title shoppingCartItemTitle parrafo_carta titu  ml-3 mb-0">${itemTitle}</h6>
            
            </div>
        </div>

        <div class="col-2">
            <div class="shopping-cart-price d-flex align-items-center h-100 border-bottom pb-2 pt-3">
                <p  class=" col-md-12 item-price mb-0 precioItem">${itemPrice}</p>
            </div>
        </div>

        <div class="col-4">
            <div
                class="shopping-cart-quantity d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">
                <input class="shopping-cart-quantity-input cantidadTitulos" type="number"
                    value="1">
                <button class="btn btn-danger buttonDelete" type="button">X</button>
            </div>
        </div>
    </div>`
    ;

    fila.innerHTML = contenidoDiv;
    divcarro.append(fila);

    fila.querySelector('.buttonDelete').addEventListener('click', deleteClick);

    fila.querySelector('.cantidadTitulos').addEventListener('change', cambioCantidad);

    actualizarTotal();

    

    let at = nodeToString(divcarro);
    var bo = 'superDiv';
    actualizarlocal(bo,at);
}


function actualizarTotal() {
    let total = 0;
    const compraTotal = document.querySelector('.totalCompra');
    //console.log("actualizarTotal -> compraTotal", compraTotal)

    const itemDelCarrito = document.querySelectorAll('.itemsDelCarrito');
    //console.log("actualizarTotal -> itemDelCarrito", itemDelCarrito)

    itemDelCarrito.forEach((itemDelCarrito) => {
        const precioDelItem = itemDelCarrito.querySelector('.precioItem');
        const precioSolo = Number(precioDelItem.textContent.replace('$', ''));
        //console.log("actualizarTotal -> precioSolo", precioSolo)
        const cantidadDelItem = itemDelCarrito.querySelector('.cantidadTitulos');
        const soloCantidad = Number(cantidadDelItem.value);
        //console.log("actualizarTotal -> soloCantidad", soloCantidad)
        total = total + precioSolo * soloCantidad;
    });

    let tt = total;
    var oo = 'preciocompra';
    actualizarlocal(oo,tt);

    compraTotal.innerHTML = `$${total.toFixed(2)}`;

}

function deleteClick(event) {

    const delClick = event.target;
    delClick.closest('.itemsDelCarrito').remove();

    actualizarTotal();

};

function cambioCantidad(event) {

    const input = event.target;

    if (input.value <= 0) { input.value = 1; }
    if (input.value >= 51) { input.value = 50; }
    actualizarTotal();

};

function clickcomprar() {

    divcarro.innerHTML = ``;
    actualizarTotal();
};





function actualizarlocal(oo,tt){
    
    localStorage.setItem(oo, tt);
};

function  idpre(){
    let superDiv = localStorage.getItem("superDiv");
    let prec = localStorage.getItem("preciocompra");

    document.getElementById("owo").innerHTML = `${superDiv}`;
    document.getElementById("precioid").innerHTML = ` $${prec} `;

    }


function nodeToString ( node ) {
    var tmpNode = document.createElement( "div" );
    tmpNode.appendChild( node.cloneNode( true ) );
    var str = tmpNode.innerHTML;
    tmpNode = node = null; // prevent memory leaks in IE
    return str;
    }