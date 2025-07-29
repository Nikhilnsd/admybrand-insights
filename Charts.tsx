'use client';

import { useState } from 'react';
import {
  LineChart,
  Line,
  AreaChart,
  Area,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';
import { motion } from 'framer-motion';
import { TrendingUp, BarChart3, PieChart as PieIcon, Activity } from 'lucide-react';
import { MetricData, CampaignData } from '@/data/mockData';
import { formatCurrency, formatNumber } from '@/lib/utils';

const COLORS = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6'];

interface ChartsProps {
  data: MetricData[];
  campaignData: CampaignData[];
}

export function Charts({ data, campaignData }: ChartsProps) {
  const [activeChart, setActiveChart] = useState<'revenue' | 'users' | 'conversions'>('revenue');

  // Prepare data for line/area charts (daily aggregates)
  const dailyData = data.reduce((acc, item) => {
    const existingDay = acc.find(d => d.date === item.date);
    if (existingDay) {
      existingDay.revenue += item.revenue;
      existingDay.users += item.users;
      existingDay.conversions += item.conversions;
    } else {
      acc.push({
        date: item.date,
        revenue: item.revenue,
        users: item.users,
        conversions: item.conversions,
      });
    }
    return acc;
  }, [] as any[]).slice(-14); // Last 14 days

  // Prepare data for campaign performance
  const campaignChartData = campaignData.map(campaign => ({
    name: campaign.campaign,
    revenue: campaign.revenue,
    users: campaign.users,
    conversions: campaign.conversions,
  }));

  const CustomTooltip = ({ active, payload, label }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="glass-effect rounded-lg p-3 border border-white/20">
          <p className="text-sm font-medium text-gray-900 dark:text-white">
            {label}
          </p>
          {payload.map((entry: any, index: number) => (
            <p key={index} className="text-sm" style={{ color: entry.color }}>
              {entry.name}: {
                entry.name === 'revenue' 
                  ? formatCurrency(entry.value)
                  : formatNumber(entry.value)
              }
            </p>
          ))}
        </div>
      );
    }
    return null;
  };

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
      {/* Revenue Trend Chart */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.1 }}
        className="glass-effect rounded-xl p-6"
      >
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <TrendingUp className="w-5 h-5 text-blue-600" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
              Revenue Trend
            </h3>
          </div>
        </div>
        <ResponsiveContainer width="100%" height={250}>
          <AreaChart data={dailyData}>
            <defs>
              <linearGradient id="revenueGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#3B82F6" stopOpacity={0.3}/>
                <stop offset="95%" stopColor="#3B82F6" stopOpacity={0}/>
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" opacity={0.3} />
            <XAxis 
              dataKey="date" 
              tick={{ fontSize: 12 }}
              tickFormatter={(value) => new Date(value).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
            />
            <YAxis tick={{ fontSize: 12 }} tickFormatter={(value) => `$${value}`} />
            <Tooltip content={<CustomTooltip />} />
            <Area
              type="monotone"
              dataKey="revenue"
              stroke="#3B82F6"
              strokeWidth={2}
              fill="url(#revenueGradient)"
            />
          </AreaChart>
        </ResponsiveContainer>
      </motion.div>

      {/* Campaign Performance Bar Chart */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.2 }}
        className="glass-effect rounded-xl p-6"
      >
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <BarChart3 className="w-5 h-5 text-green-600" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
              Campaign Performance
            </h3>
          </div>
        </div>
        <ResponsiveContainer width="100%" height={250}>
          <BarChart data={campaignChartData}>
            <CartesianGrid strokeDasharray="3 3" opacity={0.3} />
            <XAxis dataKey="name" tick={{ fontSize: 12 }} />
            <YAxis tick={{ fontSize: 12 }} tickFormatter={(value) => `$${value}`} />
            <Tooltip content={<CustomTooltip />} />
            <Bar dataKey="revenue" fill="#10B981" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </motion.div>

      {/* Conversion Distribution Pie Chart */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.3 }}
        className="glass-effect rounded-xl p-6"
      >
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <PieIcon className="w-5 h-5 text-purple-600" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
              Conversion Distribution
            </h3>
          </div>
        </div>
        <ResponsiveContainer width="100%" height={250}>
          <PieChart>
            <Pie
              data={campaignChartData}
              cx="50%"
              cy="50%"
              innerRadius={60}
              outerRadius={100}
              paddingAngle={5}
              dataKey="conversions"
            >
              {campaignChartData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip
              formatter={(value) => [formatNumber(Number(value)), 'Conversions']}
            />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </motion.div>

      {/* Multi-Metric Line Chart */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.4 }}
        className="glass-effect rounded-xl p-6"
      >
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <Activity className="w-5 h-5 text-orange-600" />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
              Multi-Metric Overview
            </h3>
          </div>
        </div>
        <ResponsiveContainer width="100%" height={250}>
          <LineChart data={dailyData}>
            <CartesianGrid strokeDasharray="3 3" opacity={0.3} />
            <XAxis 
              dataKey="date" 
              tick={{ fontSize: 12 }}
              tickFormatter={(value) => new Date(value).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
            />
            <YAxis yAxisId="left" tick={{ fontSize: 12 }} />
            <YAxis yAxisId="right" orientation="right" tick={{ fontSize: 12 }} />
            <Tooltip content={<CustomTooltip />} />
            <Legend />
            <Line
              yAxisId="left"
              type="monotone"
              dataKey="users"
              stroke="#3B82F6"
              strokeWidth={2}
              dot={{ r: 4 }}
              name="Users"
            />
            <Line
              yAxisId="right"
              type="monotone"
              dataKey="conversions"
              stroke="#10B981"
              strokeWidth={2}
              dot={{ r: 4 }}
              name="Conversions"
            />
          </LineChart>
        </ResponsiveContainer>
      </motion.div>
    </div>
  );
}
