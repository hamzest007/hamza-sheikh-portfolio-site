import Link from "next/link";
export default function NotFound() { return <main className="not-found"><div><span className="eyebrow">404</span><h1>That page wandered off.</h1><p>The project you&apos;re looking for isn&apos;t in the current portfolio inventory.</p><Link className="button button-primary" href="/">Back home</Link></div></main>; }
