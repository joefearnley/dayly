<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Carbon\Carbon;

class Entry extends Model
{
    /** @use HasFactory<\Database\Factories\EntryFactory> */
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<string>
     */
    protected $fillable = [
        'user_id',
        'slug',
        'body',
        'date_published',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array<string, string>
     */
    protected $casts = [
        'date_published' => 'datetime',
    ];

    /**
     * Get the date_published attribute in a formatted way.
     *
     * @param  string|null  $value
     * @return string|null
     */
    protected function getDatePublishedAttribute($value): ?string
    {
        return $value ? Carbon::parse($value)->format('m/d/Y') : null;
    }

    /**
     * Get the user that owns the entry.
     */
    protected function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    /**
     * Get the date_published attribute for the form.
     *
     * @return string|null
     */
    public function datePublishedForForm(): ?string
    {
        return Carbon::parse($this->date_published)->format('Y-m-d');
    }
}
