import {useState, useEffect} from "react";

export function ScrollToTopButton() {
    const [isVisible, setIsVisible] = useState(false);

    // Função para rolar a página para o topo
    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    };

    // Lógica para mostrar/esconder o botão
    useEffect(() => {
        const toggleVisibility = () => {
            // Mostrar o botão se o scroll for maior que 300px
            if (window.scrollY > 300) {
                setIsVisible(true);
            } else {
                setIsVisible(false);
            }
        };

        window.addEventListener("scroll", toggleVisibility);

        return () => {
            window.removeEventListener("scroll", toggleVisibility);
        };
    }, []);

    return (
        <button
            className={`scroll-to-top-button ${isVisible ? "visible" : ""}`}
            onClick={scrollToTop}
            title="Voltar ao Topo"
        >
            &#x25B2; {/* Seta para cima */}
        </button>
    );
}
