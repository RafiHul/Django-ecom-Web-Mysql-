document.addEventListener("DOMContentLoaded", function () {
    const beliSekarangButton = document.getElementById('beliSekarangButton');
    const beliSekarangPopup = document.getElementById('beliSekarangPopup');
    const konfirmasiBeliButton = document.getElementById('konfirmasiBeliButton');
    const jumlahBeli = document.getElementById('jumlahBeli');
    const errorText = document.getElementById('errorText');

    beliSekarangButton.addEventListener('click', () => {
        beliSekarangPopup.classList.remove('hidden');
    });

    konfirmasiBeliButton.addEventListener('click', () => {
        const jumlah = parseInt(jumlahBeli.value, 10);
        const jumlahProduk = parseInt('{{ produk.jumlah }}', 10);

        if (isNaN(jumlah) || jumlah <= 0) {
            errorText.textContent = 'Masukkan jumlah yang valid (angka positif).';
            errorText.style.display = 'block';
        } else if (jumlah > jumlahProduk) {
            errorText.textContent = 'Produk hanya tersedia ' + jumlahProduk;
            errorText.style.display = 'block';
        } else {
            errorText.style.display = 'none';
            const checkoutURL = "{% url 'items:detail' produk.id %}";

            window.location.href = checkoutURL;

            beliSekarangPopup.classList.add('hidden');
        }
    });
});