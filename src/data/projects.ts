export type Project = {
  slug: string;
  name: string;
  category: string;
  status: string;
  summary: string;
  detail: string;
  stack: string[];
  repo: string;
  accent: string;
  image?: string;
  images?: string[];
  featured?: boolean;
  verified: string;
};

export const projects: Project[] = [
  {
    slug: "connectly",
    name: "Connectly",
    category: "Mobile + Backend",
    status: "In progress",
    summary: "A React Native social app shaped around a modular TypeScript and Express backend.",
    detail: "The repository includes a mobile client, a modular TypeScript and Express backend, and a dedicated Vite admin center. The platform covers authentication, posts, comments, reactions, saved posts, users, friends, groups, notifications, moderation, verification, analytics, configuration, and audit logs. It is presented as in progress because the repository documentation describes the product scope and delivery status rather than a finished public release.",
    stack: ["React Native", "TypeScript", "Express", "MongoDB"],
    repo: "https://github.com/hamzest007/Connectly",
    accent: "violet",
    image: "/images/projects/connectly/home.png",
    images: ["/images/projects/connectly/home.png", "/images/projects/connectly/reels.png", "/images/projects/connectly/create.png", "/images/projects/connectly/notifications.png", "/images/projects/connectly/menu.png", "/images/projects/connectly/admin-overview.png"],
    featured: true,
    verified: "Private repository review",
  },
  {
    slug: "bookmint",
    name: "BookMint",
    category: "Mobile App",
    status: "In progress",
    summary: "A React Native reading platform for discovering, reading, uploading, and discussing books.",
    detail: "The BookMint repository includes home discovery, trending and top-rated books, a personal library, PDF reading, uploads, notifications, profiles, search, book chat, and socket-backed services. It also connects to public book data and AI-assisted book chat services. It is included as in progress because the repository is a working React Native codebase rather than a documented public release.",
    stack: ["React Native", "TypeScript", "React Navigation", "Socket.IO", "PDF"],
    repo: "https://github.com/hamzest007/BookMint",
    accent: "violet",
    featured: true,
    verified: "Private repository review",
  },
  {
    slug: "empire-rise",
    name: "Empire Rise",
    category: "Mobile Game",
    status: "Playable build",
    summary: "An original single-player investor-tycoon game with a deterministic virtual economy.",
    detail: "The app models company acquisition, upgrades, fictional markets, property, missions, achievements, offline earnings, and local persistence. The implementation is organized around a deterministic economy engine, typed store actions, save validation, and a five-tab navigation shell.",
    stack: ["React Native", "TypeScript", "Zustand", "MMKV"],
    repo: "https://github.com/hamzest007/RichLifeSimulator",
    accent: "amber",
    image: "/images/projects/empire-rise/home.png",
    images: ["/images/projects/empire-rise/home.png", "/images/projects/empire-rise/companies.png", "/images/projects/empire-rise/markets.png", "/images/projects/empire-rise/assets.png", "/images/projects/empire-rise/profile.png"],
    featured: true,
    verified: "Private repository review",
  },
  {
    slug: "prifina",
    name: "Prifina",
    category: "Mobile App",
    status: "In progress",
    summary: "A React Native app exploring document, media, and data-driven mobile flows.",
    detail: "The codebase uses React Navigation, React Query, Firebase Firestore, Zustand, forms, audio recording, image selection, and document picking. It is kept separate from the featured case studies until the product scope and release status are confirmed.",
    stack: ["React Native", "Firebase", "React Query", "Zustand"],
    repo: "https://github.com/hamzest007/Prifina",
    accent: "blue",
    verified: "Private repository review",
  },
  {
    slug: "task-management-app",
    name: "Task Management App",
    category: "Web Application",
    status: "Learning project",
    summary: "A React task management interface with routing, API requests, and feedback states.",
    detail: "The repository uses React, React Router, Axios, React Icons, and toast feedback. It is framed as a learning project because the repository documentation is still based on the Create React App starter guide.",
    stack: ["React", "React Router", "Axios", "CSS"],
    repo: "https://github.com/hamzest007/task-management-app",
    accent: "green",
    verified: "Public repository review",
  },
  {
    slug: "ecommerce-platform",
    name: "Ecommerce Platform",
    category: "Web Application",
    status: "Public repository",
    summary: "A public JavaScript e-commerce project and an early signal of Hamza’s web development direction.",
    detail: "The repository is publicly visible under hamzest007 and is identified as a JavaScript project. Its public documentation is currently starter-level, so this case study intentionally avoids claiming features that have not been confirmed.",
    stack: ["JavaScript", "React", "CSS"],
    repo: "https://github.com/hamzest007/ecommerce-platform",
    accent: "pink",
    image: "/images/ecommerce-platform.png",
    verified: "Public repository review",
  },
];

export const featuredProjects = projects.filter((project) => project.featured);
