btn_eliminar_producto = document.querySelectorAll(".btn-eliminar-producto");
console.log(btn_eliminar_producto);
btn_eliminar_producto.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    console.log(btn_eliminar_producto);
    const msg = confirm("¿Estás seguro de que deseas eliminar este producto?");
    if (!msg) {
      e.preventDefault();
    }
  });
});
