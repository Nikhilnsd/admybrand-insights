# Create app/layout.tsx (root layout)
app_layout = """import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import '../styles/globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'ADmyBRAND Insights - Analytics Dashboard',
  description: 'Modern analytics dashboard for digital marketing agencies',
  keywords: 'analytics, dashboard, marketing, data visualization, Next.js',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        {children}
      </body>
    </html>
  );
}
"""

# Create app/page.tsx (main page)
app_page = """'use client';

import { Sidebar } from '@/components/Sidebar';
import { Dashboard } from '@/components/Dashboard';

export default function Home() {
  return (
    <Sidebar>
      <Dashboard />
    </Sidebar>
  );
}
"""

# Write the app files
with open(f"{project_name}/app/layout.tsx", "w") as f:
    f.write(app_layout)

with open(f"{project_name}/app/page.tsx", "w") as f:
    f.write(app_page)

print("Created Next.js App Router files:")
print("  - app/layout.tsx")
print("  - app/page.tsx")