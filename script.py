path = r'C:\Users\gabriel\Desktop\biel teste\MazyOS-main\templates\ferramentas\Site-da-metrion\code.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove Lenis initialization script and CDN reference
html = html.replace('<script src=\"https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js\"></script>', '')

lenis_block = '''
  <!-- Lenis & GSAP Initialization -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // Initialize GSAP ScrollTrigger if available
      if (window.gsap && window.ScrollTrigger) {
        gsap.registerPlugin(ScrollTrigger);

        // Fade up reveal for sections
        gsap.utils.toArray('section').forEach((section) => {
          gsap.from(section.querySelectorAll('.glass-card, h2, p'), {
            scrollTrigger: {
              trigger: section,
              start: 'top 85%',
              toggleActions: 'play none none none'
            },
            y: 30,
            opacity: 0,
            duration: 0.8,
            stagger: 0.1,
            ease: 'power2.out'
          });
        });
      }
    });
  </script>
'''

# Replace the old script block with native instant scroll + GSAP
old_script_block_start = html.find('<!-- Lenis & GSAP Initialization -->')
if old_script_block_start != -1:
    old_script_block_end = html.find('</body>', old_script_block_start)
    html = html[:old_script_block_start] + lenis_block + html[old_script_block_end:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Removed Lenis and restored 100% native instant mouse responsiveness!')
