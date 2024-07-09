document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.filters input');
    const cards = document.querySelectorAll('.cards .card');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const category = button.value.trim();

            cards.forEach(card => {
                const cardCategory = card.getAttribute('data-category').trim();

                if (category === 'Todo') {
                    card.style.display = 'block';
                } else if (cardCategory === category) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});


