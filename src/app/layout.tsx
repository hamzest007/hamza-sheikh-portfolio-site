import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Hamza Sheikh — Frontend & React Native Developer",
  description: "Hamza Sheikh is a frontend and React Native developer building responsive web and mobile applications.",
  metadataBase: new URL("https://hamza-sheikh-portfolio-650.netlify.app"),
  openGraph: {
    title: "Hamza Sheikh — Frontend & React Native Developer",
    description: "Building responsive web products and React Native applications.",
    type: "website",
  },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
