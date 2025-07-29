# Create Sidebar component
sidebar_component = """'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import {
  BarChart3,
  Users,
  TrendingUp,
  Settings,
  Menu,
  X,
  Home,
  Target,
  DollarSign,
} from 'lucide-react';
import { ThemeToggle } from './ThemeToggle';

const navigation = [
  { name: 'Dashboard', icon: Home, current: true },
  { name: 'Analytics', icon: BarChart3, current: false },
  { name: 'Campaigns', icon: Target, current: false },
  { name: 'Revenue', icon: DollarSign, current: false },
  { name: 'Users', icon: Users, current: false },
  { name: 'Trends', icon: TrendingUp, current: false },
  { name: 'Settings', icon: Settings, current: false },
];

interface SidebarProps {
  children: React.ReactNode;
}

export function Sidebar({ children }: SidebarProps) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="flex h-screen bg-gray-50 dark:bg-gray-900">
      {/* Mobile sidebar overlay */}
      {sidebarOpen && (
        <div
          className="fixed inset-0 z-40 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        >
          <div className="absolute inset-0 bg-black opacity-50" />
        </div>
      )}

      {/* Sidebar */}
      <motion.div
        initial={false}
        animate={{
          x: sidebarOpen ? 0 : '-100%',
        }}
        className={`fixed inset-y-0 left-0 z-50 w-64 bg-white dark:bg-gray-800 shadow-lg lg:static lg:translate-x-0 lg:shadow-none`}
      >
        <div className="flex h-full flex-col">
          {/* Logo */}
          <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200 dark:border-gray-700">
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <BarChart3 className="w-5 h-5 text-white" />
              </div>
              <span className="text-xl font-bold text-gray-900 dark:text-white">
                ADmyBRAND
              </span>
            </div>
            <button
              onClick={() => setSidebarOpen(false)}
              className="lg:hidden p-1 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Navigation */}
          <nav className="flex-1 px-4 py-6 space-y-2">
            {navigation.map((item) => {
              const Icon = item.icon;
              return (
                <a
                  key={item.name}
                  href="#"
                  className={`flex items-center space-x-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                    item.current
                      ? 'bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300'
                      : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
                  }`}
                >
                  <Icon className="w-5 h-5" />
                  <span>{item.name}</span>
                </a>
              );
            })}
          </nav>

          {/* Bottom section */}
          <div className="px-4 py-4 border-t border-gray-200 dark:border-gray-700">
            <div className="flex items-center justify-between">
              <div className="text-sm text-gray-600 dark:text-gray-400">
                Theme
              </div>
              <ThemeToggle />
            </div>
            <div className="mt-4 text-xs text-gray-500 dark:text-gray-400">
              © 2025 ADmyBRAND Insights
            </div>
          </div>
        </div>
      </motion.div>

      {/* Main content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Top bar */}
        <header className="bg-white dark:bg-gray-800 shadow-sm border-b border-gray-200 dark:border-gray-700">
          <div className="flex items-center justify-between px-6 py-4">
            <button
              onClick={() => setSidebarOpen(true)}
              className="lg:hidden p-2 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700"
            >
              <Menu className="w-5 h-5" />
            </button>
            <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
              Analytics Dashboard
            </h1>
            <div className="flex items-center space-x-4">
              <div className="hidden sm:block text-sm text-gray-600 dark:text-gray-400">
                Last updated: {new Date().toLocaleTimeString()}
              </div>
            </div>
          </div>
        </header>

        {/* Main content area */}
        <main className="flex-1 overflow-auto p-6">
          {children}
        </main>
      </div>
    </div>
  );
}
"""

# Create main Dashboard component
dashboard_component = """'use client';

import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { 
  DollarSign, 
  Users, 
  Target, 
  TrendingUp,
  RefreshCw 
} from 'lucide-react';
import { MetricCard } from './MetricCard';
import { Charts } from './Charts';
import { DataTable } from './DataTable';
import { CardSkeleton, ChartSkeleton } from './LoadingSkeleton';
import { mockData, campaignData, summaryMetrics } from '@/data/mockData';
import { formatCurrency, formatNumber, formatPercentage, calculateGrowth } from '@/lib/utils';

export function Dashboard() {
  const [isLoading, setIsLoading] = useState(true);
  const [isRealTimeEnabled, setIsRealTimeEnabled] = useState(false);
  const [lastUpdated, setLastUpdated] = useState(new Date());

  // Simulate loading
  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 1500);

    return () => clearTimeout(timer);
  }, []);

  // Real-time updates simulation
  useEffect(() => {
    if (!isRealTimeEnabled) return;

    const interval = setInterval(() => {
      setLastUpdated(new Date());
      // In a real app, you would fetch new data here
    }, 5000);

    return () => clearInterval(interval);
  }, [isRealTimeEnabled]);

  // Calculate growth percentages (simulated)
  const growthMetrics = {
    revenue: calculateGrowth(summaryMetrics.totalRevenue, summaryMetrics.totalRevenue * 0.9),
    users: calculateGrowth(summaryMetrics.totalUsers, summaryMetrics.totalUsers * 0.85),
    conversions: calculateGrowth(summaryMetrics.totalConversions, summaryMetrics.totalConversions * 0.95),
    conversionRate: calculateGrowth(summaryMetrics.conversionRate, summaryMetrics.conversionRate * 0.88),
  };

  if (isLoading) {
    return (
      <div className="space-y-6">
        {/* Skeleton for metric cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {Array.from({ length: 4 }).map((_, i) => (
            <CardSkeleton key={i} />
          ))}
        </div>
        
        {/* Skeleton for charts */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {Array.from({ length: 4 }).map((_, i) => (
            <ChartSkeleton key={i} />
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Real-time toggle */}
      <div className="flex justify-between items-center">
        <h2 className="text-3xl font-bold text-gray-900 dark:text-white">
          Dashboard Overview
        </h2>
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-2">
            <label className="text-sm font-medium text-gray-700 dark:text-gray-300">
              Real-time Updates
            </label>
            <button
              onClick={() => setIsRealTimeEnabled(!isRealTimeEnabled)}
              className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
                isRealTimeEnabled ? 'bg-blue-600' : 'bg-gray-200 dark:bg-gray-700'
              }`}
            >
              <span
                className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                  isRealTimeEnabled ? 'translate-x-6' : 'translate-x-1'
                }`}
              />
            </button>
          </div>
          {isRealTimeEnabled && (
            <div className="flex items-center space-x-2 text-sm text-green-600 dark:text-green-400">
              <RefreshCw className="w-4 h-4 animate-spin" />
              <span>Live</span>
            </div>
          )}
        </div>
      </div>

      {/* Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard
          title="Total Revenue"
          value={formatCurrency(summaryMetrics.totalRevenue)}
          change={growthMetrics.revenue}
          icon={<DollarSign className="w-6 h-6" />}
        />
        <MetricCard
          title="Total Users"
          value={formatNumber(summaryMetrics.totalUsers)}
          change={growthMetrics.users}
          icon={<Users className="w-6 h-6" />}
        />
        <MetricCard
          title="Conversions"
          value={formatNumber(summaryMetrics.totalConversions)}
          change={growthMetrics.conversions}
          icon={<Target className="w-6 h-6" />}
        />
        <MetricCard
          title="Conversion Rate"
          value={formatPercentage(summaryMetrics.conversionRate)}
          change={growthMetrics.conversionRate}
          icon={<TrendingUp className="w-6 h-6" />}
        />
      </div>

      {/* Charts */}
      <Charts data={mockData} campaignData={campaignData} />

      {/* Data Table */}
      <DataTable data={campaignData} />

      {/* Footer info */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.8 }}
        className="text-center text-sm text-gray-500 dark:text-gray-400 mt-8"
      >
        Last updated: {lastUpdated.toLocaleString()} | 
        Data refreshes every {isRealTimeEnabled ? '5 seconds' : 'manual refresh'}
      </motion.div>
    </div>
  );
}
"""

# Write the components
with open(f"{project_name}/components/Sidebar.tsx", "w") as f:
    f.write(sidebar_component)

with open(f"{project_name}/components/Dashboard.tsx", "w") as f:
    f.write(dashboard_component)

print("Created layout and dashboard components:")
print("  - components/Sidebar.tsx")
print("  - components/Dashboard.tsx")