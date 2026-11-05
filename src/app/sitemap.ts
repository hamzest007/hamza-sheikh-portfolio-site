import type { MetadataRoute } from "next";
import { projects } from "@/data/projects";
export default function sitemap(): MetadataRoute.Sitemap { return [{ url: "https://hamzest007.github.io", lastModified: new Date() }, ...projects.map((project) => ({ url: `https://hamzest007.github.io/projects/${project.slug}`, lastModified: new Date() }))]; }
