# Hamza Sheikh — Interactive Developer Portfolio

![Portfolio preview](public/images/hamza-sheikh.jpg)

An interactive, full-screen developer portfolio presented as a modern 3D storybook. It introduces Hamza Sheikh’s frontend and React Native work through animated chapters, project links, a professional portfolio view, and responsive layouts.

## Live site

- [Open the portfolio](https://hamza-sheikh-portfolio-650.netlify.app)
- [GitHub repository](https://github.com/hamzest007/hamza-sheikh-portfolio-site)
- [LinkedIn](https://www.linkedin.com/in/hamza-sheikh-3a551231b/)

## Features

- Full-screen cartoon-inspired 3D book cover and reader
- Animated page turns with chapter navigation
- About, projects, skills, services, journey, experience, education, and contact chapters
- Touch swipe, mouse, keyboard arrow, and Enter/Space navigation
- Progress indicator and page counter
- Real project repository links and verified project screenshots
- Professional portfolio fallback view
- Responsive desktop, tablet, and mobile layouts
- Downloadable CV link
- Reduced-motion support for accessibility

## Featured projects

The portfolio references verified project information from Hamza’s GitHub work:

- [Connectly](https://github.com/hamzest007/Connectly) — React Native social platform with TypeScript and Express.
- [BookMint](https://github.com/hamzest007/BookMint) — React Native reading platform.
- [Empire Rise](https://github.com/hamzest007/RichLifeSimulator) — React Native investor-tycoon simulator.
- [Prifina](https://github.com/hamzest007/Prifina) — React Native data and media flows.
- [Task Management App](https://github.com/hamzest007/task-management-app) — React task management interface.
- [Ecommerce Platform](https://github.com/hamzest007/ecommerce-platform) — JavaScript e-commerce project.

## Technology

- Next.js 15
- React 19
- JavaScript and TypeScript
- CSS 3D transforms and responsive CSS
- Lucide React icons
- Netlify deployment

## Run locally

### Requirements

- Node.js 20 or newer
- npm

### Installation

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Production build

```bash
npm run build
npm run start
```

## Project structure

```text
src/
├── app/
│   ├── projects/[slug]/   # Project detail pages
│   ├── globals.css        # Portfolio and 3D book styling
│   └── page.tsx           # Homepage entry
├── components/
│   ├── DeveloperStorybook.jsx
│   └── Reveal.tsx
└── data/
    └── projects.ts        # Verified project data and links
public/
├── images/                # Portfolio and project imagery
└── resume/                # Downloadable CV
```

## Contact

Hamza Sheikh is a frontend and React Native developer based in Karachi, Pakistan.

- Email: [hamzasheikh4000@gmail.com](mailto:hamzasheikh4000@gmail.com)
- GitHub: [@hamzest007](https://github.com/hamzest007)
- LinkedIn: [Hamza Sheikh](https://www.linkedin.com/in/hamza-sheikh-3a551231b/)

## License

This portfolio is personal work by Hamza Sheikh. Project names, screenshots, and linked repositories remain subject to their respective owners and repository licenses.
