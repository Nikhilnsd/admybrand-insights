'use client';

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
