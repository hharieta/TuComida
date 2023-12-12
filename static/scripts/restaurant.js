const categories = document.querySelectorAll('.category');
        const contentSections = document.querySelectorAll('.category-content');

        categories.forEach((category, index) => {
            category.addEventListener("click", () => {
                categories.forEach((c) => c.classList.remove('active'));
                contentSections.forEach((section) => section.style.display = "none");

                category.classList.add('active');
                contentSections[index].style.display = "block";
            });
        });

        document.addEventListener("DOMContentLoaded", function () {
            // Evento de clic para la pestaña "Todos"
            document.getElementById("all-tab").addEventListener("click", function () {
                // Limpia el contenido existente en "all-content"
                document.getElementById("all-content").innerHTML = "";

                // Copia el contenido de la pestaña "Adultos"
                var adultsContent = document.getElementById("adults-content").innerHTML;
                document.getElementById("all-content").innerHTML += adultsContent;

                // Copia el contenido de la pestaña "Niños"
                var kidsContent = document.getElementById("kids-content").innerHTML;
                document.getElementById("all-content").innerHTML += kidsContent;

                // Copia el contenido de la pestaña "Saludable"
                var healthyContent = document.getElementById("healthy-content").innerHTML;
                document.getElementById("all-content").innerHTML += healthyContent;
            });

            // Simular un clic en la pestaña "Todos" al cargar la página
            document.getElementById("all-tab").click();
        });

                // foto perfil /restaurant.js

                /*
document.addEventListener('DOMContentLoaded', function () {
    const profilePhotoInput = document.getElementById('profile-photo-input');
    const profilePhotoBtn = document.getElementById('profile-photo-btn');

    profilePhotoBtn.addEventListener('click', function () {
        profilePhotoInput.click();
    });

    profilePhotoInput.addEventListener('change', function () {
        const file = profilePhotoInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                const profilePhoto = document.getElementById('profile-photo-btn');
                profilePhoto.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
});
**/

document.addEventListener('DOMContentLoaded', function () {
    const profilePhotoInput = document.getElementById('profile-photo-input');
    const profilePhotoBtn = document.getElementById('profile-photo-btn');

    profilePhotoBtn.addEventListener('click', function () {
        console.log('Clic en el botón de la foto de perfil');
        profilePhotoInput.click();
    });

    profilePhotoInput.addEventListener('change', function () {
      
    });
});


//MOdal PaREDES


function openModal(modalId) {
    var modal = document.getElementById(modalId);
    if (modal) {
        modal.style.opacity = 1;
        modal.style.pointerEvents = 'auto';
    }
}

function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    if (modal) {
        modal.style.opacity = 0;
        modal.style.pointerEvents = 'none';
    }
}
 

//cerrar
document.querySelectorAll('.close').forEach(function (closeButton) {
    closeButton.addEventListener('click', function () {
        var modalId = this.getAttribute('data-modal');
        closeModal(modalId);
    });
});

function submitAndCloseModal(modalId) {
    alert('YA LO HACKEAMOS');
    closeModal(modalId);
}



/**IMAGeN JS */s

function previewImage() {
    var input = document.getElementById('imageInput');
    var preview = document.getElementById('imagePreview');

    
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            // previsual
            preview.innerHTML = '<img src="' + e.target.result + '" alt="Image Preview">';
        };

        reader.readAsDataURL(input.files[0]);
    } else {
        preview.innerHTML = '';
    }
}
