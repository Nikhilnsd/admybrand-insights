'use client';

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
