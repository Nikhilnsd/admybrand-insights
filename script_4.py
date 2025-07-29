# Create MetricCard component
metric_card = """'use client';

import { motion } from 'framer-motion';
import { TrendingUp, TrendingDown } from 'lucide-react';
import { cn } from '@/lib/utils';

interface MetricCardProps {
  title: string;
  value: string;
  change?: number;
  icon: React.ReactNode;
  className?: string;
}

export function MetricCard({ title, value, change, icon, className }: MetricCardProps) {
  const isPositive = change && change > 0;
  const isNegative = change && change < 0;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      className={cn(
        "glass-effect rounded-xl p-6 hover:scale-105 transition-all duration-200",
        className
      )}
    >
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="p-2 rounded-lg bg-blue-500/20 text-blue-600 dark:text-blue-400">
            {icon}
          </div>
          <div>
            <p className="text-sm text-gray-600 dark:text-gray-400">{title}</p>
            <p className="text-2xl font-bold text-gray-900 dark:text-white">{value}</p>
          </div>
        </div>
        {change !== undefined && (
          <div className={cn(
            "flex items-center space-x-1 text-sm font-medium",
            isPositive && "text-green-600",
            isNegative && "text-red-600",
            !isPositive && !isNegative && "text-gray-600"
          )}>
            {isPositive && <TrendingUp className="w-4 h-4" />}
            {isNegative && <TrendingDown className="w-4 h-4" />}
            <span>{Math.abs(change).toFixed(1)}%</span>
          </div>
        )}
      </div>
    </motion.div>
  );
}
"""

# Create ThemeToggle component
theme_toggle = """'use client';

import { useState, useEffect } from 'react';
import { Sun, Moon } from 'lucide-react';
import { motion } from 'framer-motion';

export function ThemeToggle() {
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    // Check if theme is stored in localStorage
    const stored = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (stored === 'dark' || (!stored && prefersDark)) {
      setIsDark(true);
      document.documentElement.classList.add('dark');
    }
  }, []);

  const toggleTheme = () => {
    const newTheme = !isDark;
    setIsDark(newTheme);
    
    if (newTheme) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  };

  return (
    <motion.button
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      onClick={toggleTheme}
      className="p-2 rounded-lg glass-effect hover:bg-white/20 dark:hover:bg-black/20 transition-colors"
      aria-label="Toggle theme"
    >
      {isDark ? (
        <Sun className="w-5 h-5 text-yellow-500" />
      ) : (
        <Moon className="w-5 h-5 text-blue-600" />
      )}
    </motion.button>
  );
}
"""

# Create LoadingSkeleton component
loading_skeleton = """'use client';

import { cn } from '@/lib/utils';

interface LoadingSkeletonProps {
  className?: string;
  rows?: number;
}

export function LoadingSkeleton({ className, rows = 1 }: LoadingSkeletonProps) {
  return (
    <div className={cn("animate-pulse", className)}>
      {Array.from({ length: rows }).map((_, i) => (
        <div
          key={i}
          className="h-4 bg-gray-300 dark:bg-gray-700 rounded mb-2 last:mb-0"
        />
      ))}
    </div>
  );
}

export function CardSkeleton() {
  return (
    <div className="glass-effect rounded-xl p-6 animate-pulse">
      <div className="flex items-center space-x-3">
        <div className="w-10 h-10 bg-gray-300 dark:bg-gray-700 rounded-lg" />
        <div className="flex-1">
          <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded mb-2" />
          <div className="h-6 bg-gray-300 dark:bg-gray-700 rounded w-24" />
        </div>
      </div>
    </div>
  );
}

export function ChartSkeleton() {
  return (
    <div className="glass-effect rounded-xl p-6 animate-pulse">
      <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded mb-4 w-32" />
      <div className="h-64 bg-gray-300 dark:bg-gray-700 rounded" />
    </div>
  );
}
"""

# Write component files
with open(f"{project_name}/components/MetricCard.tsx", "w") as f:
    f.write(metric_card)

with open(f"{project_name}/components/ThemeToggle.tsx", "w") as f:
    f.write(theme_toggle)

with open(f"{project_name}/components/LoadingSkeleton.tsx", "w") as f:
    f.write(loading_skeleton)

print("Created UI components:")
print("  - components/MetricCard.tsx")
print("  - components/ThemeToggle.tsx")
print("  - components/LoadingSkeleton.tsx")