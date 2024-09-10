/*
document.addEventListener('DOMContentLoaded', function() {
    var accordionButtons = document.querySelectorAll('.accordion-button');
    
    accordionButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            
            var target = this.getAttribute('data-bs-target');
            var content = document.querySelector(target);
            
            // 모든 아코디언 아이템을 닫습니다
            document.querySelectorAll('.accordion-collapse.show').forEach(function(item) {
                if (item !== content) {
                    item.classList.remove('show');
                    var otherButton = document.querySelector('[data-bs-target="#' + item.id + '"]');
                    otherButton.classList.add('collapsed');
                    otherButton.setAttribute('aria-expanded', 'false');
                }
            });
            
            // 현재 아이템의 상태를 토글합니다
            if (content.classList.contains('show')) {
                content.classList.remove('show');
                this.classList.add('collapsed');
                this.setAttribute('aria-expanded', 'false');
            } else {
                content.classList.add('show');
                this.classList.remove('collapsed');
                this.setAttribute('aria-expanded', 'true');
            }
        });
    });
});
*/