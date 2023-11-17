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