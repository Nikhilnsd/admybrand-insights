'use client';

import { Sidebar } from '@/components/Sidebar';
import { Dashboard } from '@/components/Dashboard';

export default function Home() {
  return (
    <Sidebar>
      <Dashboard />
    </Sidebar>
  );
}
