/* ==========================================================================
   Vignesh Portfolio - Main JavaScript
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const navMenu = document.getElementById('nav-menu');
    const navToggle = document.getElementById('nav-toggle');
    const navClose = document.getElementById('nav-close');
    const navLinks = document.querySelectorAll('.nav-link');

    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.add('show-menu');
        });
    }

    if (navClose) {
        navClose.addEventListener('click', () => {
            navMenu.classList.remove('show-menu');
        });
    }

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('show-menu');
        });
    });

    // 2. Dynamic Typing Text Effect
    const typingElement = document.querySelector('.typing-text');
    if (typingElement) {
        const wordsData = typingElement.getAttribute('data-words');
        const words = wordsData ? JSON.parse(wordsData) : [
            "Full-Stack Django Applications",
            "JavaScript Web Systems",
            "Relational SQL Databases",
            "Embedded & IoT Solutions"
        ];
        
        let wordIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let typeSpeed = 100;

        function type() {
            const currentWord = words[wordIndex];
            
            if (isDeleting) {
                typingElement.textContent = currentWord.substring(0, charIndex - 1);
                charIndex--;
                typeSpeed = 45;
            } else {
                typingElement.textContent = currentWord.substring(0, charIndex + 1);
                charIndex++;
                typeSpeed = 100;
            }

            if (!isDeleting && charIndex === currentWord.length) {
                isDeleting = true;
                typeSpeed = 2200; // Pause at end of word
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;
                typeSpeed = 400; // Pause before starting new word
            }

            setTimeout(type, typeSpeed);
        }

        setTimeout(type, 800);
    }

    // 3. Project Category Filter Controls
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach(card => {
                const category = card.getAttribute('data-category');
                if (filterValue === 'all' || category === filterValue || (filterValue === 'web' && (category === 'web' || category === 'frontend'))) {
                    card.style.display = 'flex';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 250);
                }
            });
        });
    });

    // 4. Scroll to Top Button Visibility & Active Link Highlighting
    const scrollTop = document.getElementById('scroll-top');
    const sections = document.querySelectorAll('section[id]');

    function scrollActions() {
        const scrollY = window.pageYOffset || document.documentElement.scrollTop;

        // Show scroll-to-top
        if (scrollTop) {
            if (scrollY >= 350) {
                scrollTop.classList.add('show-scroll');
            } else {
                scrollTop.classList.remove('show-scroll');
            }
        }

        // Active link highlighting
        sections.forEach(current => {
            const sectionHeight = current.offsetHeight;
            const sectionTop = current.offsetTop - 100;
            const sectionId = current.getAttribute('id');
            const correspondingLink = document.querySelector(`.nav-menu a[href*='${sectionId}']`);

            if (correspondingLink) {
                if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                    correspondingLink.classList.add('active-link');
                } else {
                    correspondingLink.classList.remove('active-link');
                }
            }
        });
    }

    window.addEventListener('scroll', scrollActions);
    scrollActions();

    // 5. Contact Form UX Enhancements
    const contactForm = document.getElementById('contact-form');
    const submitBtn = document.getElementById('submit-btn');

    if (contactForm && submitBtn) {
        contactForm.addEventListener('submit', () => {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending Message...';
        });
    }
});
