import {useEffect} from "react";
import {useLocation} from "react-router-dom";

export default function ScrollToTop() {
    const {pathname, hash} = useLocation();

    useEffect(() => {
        if (hash) {
            setTimeout(() => {
                const element = document.getElementById(hash.substring(1));
                if (element) {
                    const menuHeight = 12 * 16;
                    const elementPosition = element.getBoundingClientRect().top + window.scrollY;
                    const offsetPosition = elementPosition - menuHeight - 20;
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: "smooth"
                    });
                }
            }, 100);
            return;
        }
        window.scrollTo(0, 0);
    }, [pathname, hash]);
    return null;
}
