document.addEventListener("DOMContentLoaded", function () {
    const beliSekarangButton = document.getElementById('beliSekarangButton');
    const beliSekarangPopup = document.getElementById('beliSekarangPopup');
    const konfirmasiBeliButton = document.getElementById('konfirmasiBeliButton');
    const jumlahBeli = document.getElementById('jumlahBeli');

    beliSekarangButton.addEventListener('click', () => {
        beliSekarangPopup.classList.remove('hidden');
    });

    konfirmasiBeliButton.addEventListener('click', () => {
        const jumlah = parseInt(jumlahBeli.value, 10);
        const jumlahProduk = parseInt('{{ produk.jumlah }}', 10);

        if (isNaN(jumlah) || jumlah <= 0) {
            alert('Masukkan jumlah yang valid (angka positif).');
            return;
        } else if (jumlah > jumlahProduk) {
            alert('Jumlah melebihi stok produk yang tersedia.');
            return;
        } else {
            const checkoutURL = "{% url 'items:detail' produk.id %}";

            window.location.href = checkoutURL;

            beliSekarangPopup.classList.add('hidden');
        }
    });
});