<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Entry>
 */
class EntryFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        $datePublished = now()->subDays(rand(0, 30));

        return [
            'user_id' => 1,
            'body' => fake()->paragraph(2),
            'slug' => $datePublished . '-' . uniqid(),
            'date_published' => $datePublished,
        ];
    }
}
