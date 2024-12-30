async function loadProjects() {
    const response = await fetch('/api/projects');
    const projects = await response.json();
    
    const projectGrid = document.getElementById('project-grid');
    
    projects.forEach(project => {
        const projectCard = document.createElement('div');
        projectCard.className = 'project-card';
        
        projectCard.innerHTML = `
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <div class="tech-stack">
                ${project.technologies.map(tech => `<span class="tech-tag">${tech}</span>`).join('')}
            </div>
            ${project.url ? `<a href="${project.url}" target="_blank" class="project-link">View Project</a>` : ''}
            </div>
            ${project.github ? `<a href="${project.github}" target="_blank" class="project-link">View Code</a>` : ''}
            </div>
            ${project.image ? `<img src="${project.image}" alt="${project.title}" class="project-image">` : ''}
            </div>
            ${project.gif ? `<video src="${project.gif}" alt="${project.title}" class="project-image" controls></video>` : ''}
        `;
        
        projectGrid.appendChild(projectCard);
    });
}

document.addEventListener('DOMContentLoaded', loadProjects);